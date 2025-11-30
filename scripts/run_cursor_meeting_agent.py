#!/usr/bin/env python3
"""
Meeting-focused Cursor Cloud agent runner.

Reads a transcript, launches a Cursor Cloud agent via the public API, waits for
the agent to finish, and writes the resulting architecture brief to
`meeting_outputs/<slug>.md`. Falls back to a heuristic summary when the agent
cannot be reached.
"""

from __future__ import annotations

import argparse
import base64
import datetime as dt
import json
import os
import pathlib
import re
import ssl
import sys
import textwrap
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
import zipfile
from typing import Any, Dict, Optional

try:
    import PyPDF2
except ImportError:  # pragma: no cover - only triggered if dependency missing
    PyPDF2 = None

NAMESPACE = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
DEFAULT_REPOSITORY = os.getenv(
    "CURSOR_REPOSITORY", "https://github.com/godhavari-gopal-covergo/architecture"
)
DEFAULT_REF = os.getenv("CURSOR_REPOSITORY_REF", "main")
DEFAULT_OUTPUT_DIR = pathlib.Path("meeting_outputs")
DEFAULT_TRANSCRIPT_ROOT = pathlib.Path("meeting_transcripts")


class CursorApiError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Launch the meeting-summary Cursor Cloud agent for a transcript."
    )
    parser.add_argument(
        "--transcript",
        required=True,
        help="Path to the transcript (.md/.txt/.docx/.gdoc).",
    )
    parser.add_argument(
        "--output",
        help="Explicit output path. Defaults to meeting_outputs/<slug>.md.",
    )
    parser.add_argument(
        "--meeting-title",
        help="Friendly meeting title; defaults to filename.",
    )
    parser.add_argument(
        "--meeting-date",
        help="Meeting date (ISO). Defaults to transcript filename prefix or today.",
    )
    parser.add_argument(
        "--stakeholders",
        help="Comma-separated stakeholder names/roles for the prompt.",
    )
    parser.add_argument(
        "--slug",
        help="Custom slug used for the output filename.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=600,
        help="Seconds to wait for the agent to finish (default: 600).",
    )
    parser.add_argument(
        "--poll-interval",
        type=int,
        default=5,
        help="Seconds between status checks (default: 5).",
    )
    parser.add_argument(
        "--branch-name",
        help="Optional branch name to send in the agent target payload.",
    )
    return parser.parse_args()


def read_transcript(path: pathlib.Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".docx":
        return extract_docx_text(path)
    if suffix == ".pdf":
        return extract_pdf_text(path)
    if suffix in {".md", ".txt"}:
        return path.read_text(encoding="utf-8")
    if suffix == ".gdoc":
        data = json.loads(path.read_text(encoding="utf-8"))
        url = data.get("url", "https://docs.google.com/")
        message = (
            "WARNING: Google .gdoc files are Drive shortcuts.\n"
            "Please export the meeting notes as Markdown or DOCX and commit that file.\n"
            f"Referenced document: {url}"
        )
        return message
    return path.read_text(encoding="utf-8", errors="ignore")


def extract_docx_text(path: pathlib.Path) -> str:
    with zipfile.ZipFile(path) as archive:
        xml_data = archive.read("word/document.xml")
    root = ET.fromstring(xml_data)
    paragraphs = []
    for para in root.findall(".//w:p", NAMESPACE):
        texts = []
        for node in para.findall(".//w:t", NAMESPACE):
            if node.text:
                texts.append(node.text)
        if texts:
            paragraphs.append("".join(texts))
    return "\n".join(paragraphs)


def extract_pdf_text(path: pathlib.Path) -> str:
    if PyPDF2 is None:
        return (
            "PDF transcript provided, but PyPDF2 is not installed in this environment.\n"
            "Install PyPDF2 to enable extraction, or provide the transcript in Markdown/TXT/DOCX."
        )
    text = []
    with path.open("rb") as fh:
        reader = PyPDF2.PdfReader(fh)
        for page in reader.pages:
            try:
                extracted = page.extract_text() or ""
            except Exception as exc:  # pragma: no cover - PyPDF2 edge cases
                extracted = f"[Warning: failed to read a PDF page: {exc}]"
            text.append(extracted.strip())
    content = "\n\n".join(line for line in text if line)
    if not content.strip():
        return "PDF transcript contained no extractable text. Please export to Markdown or DOCX."
    return content


def slugify(text: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-")
    return safe.lower() or "meeting"


def infer_metadata(path: pathlib.Path, meeting_date: Optional[str], title: Optional[str]) -> Dict[str, str]:
    if not title:
        title = path.stem.replace("-", " ").replace("_", " ").title()
    if not meeting_date:
        match = re.match(r"(\d{4}-\d{2}-\d{2})", path.name)
        if match:
            meeting_date = match.group(1)
    if not meeting_date:
        meeting_date = dt.date.today().isoformat()
    return {"title": title, "date": meeting_date}


def build_prompt(metadata: Dict[str, str], stakeholders: Optional[str], transcript: str) -> str:
    stakeholder_text = stakeholders or "Not specified"
    return textwrap.dedent(
        f"""
        You are a principal solutions architect. Analyse the following meeting transcript
        and produce a single markdown document tailored for architecture planning.

        Meeting title: {metadata['title']}
        Meeting date: {metadata['date']}
        Stakeholders: {stakeholder_text}

        Requirements:
        - Summarize the meeting context and key decisions.
        - List business requirements, technical requirements, constraints, and assumptions.
        - Capture action items with owners and due dates if available.
        - Recommend next sessions/workshops with target attendees and agenda bullets.
        - If business/customer flows were discussed, provide a Mermaid flowchart or sequence diagram.
        - If solution or integration designs were discussed, provide a Mermaid sequence/class diagram describing system interactions.
        - Include sections: Summary, Business Requirements, Technical Requirements, Architecture / Integration Notes, Action Items, Next Steps & Upcoming Sessions, Mermaid Diagrams, Risks & Open Questions, Appendix.
        - Respond with the full markdown document in a single message. Do not reference separate files or attachments.
        - Keep the output professional and suitable for handoff to implementation teams.

        Transcript:
        ---
        {transcript}
        ---
        """
    ).strip()


def cursor_request(
    path: str,
    payload: Optional[Dict[str, Any]] = None,
    method: str = "GET",
) -> Dict[str, Any]:
    api_key = os.getenv("CURSOR_API_KEY")
    if not api_key:
        raise CursorApiError("CURSOR_API_KEY environment variable is required.")

    base_url = os.getenv("CURSOR_API_BASE", "https://api.cursor.com/v0")
    url = f"{base_url.rstrip('/')}{path}"
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    auth_header = base64.b64encode(f"{api_key}:".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/json",
    }
    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    context = None
    if os.getenv("CURSOR_SKIP_SSL_VERIFY") == "1":
        context = ssl._create_unverified_context()
    try:
        with urllib.request.urlopen(request, context=context, timeout=120) as response:
            raw = response.read().decode("utf-8")
            return json.loads(raw)
    except urllib.error.HTTPError as exc:
        raise CursorApiError(f"Cursor API error {exc.code}: {exc.read().decode('utf-8')}") from exc
    except urllib.error.URLError as exc:
        raise CursorApiError(f"Cursor API network error: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise CursorApiError(f"Invalid JSON from Cursor API: {exc}") from exc


def launch_agent(prompt: str, branch_name: Optional[str]) -> str:
    payload: Dict[str, Any] = {
        "prompt": {"text": prompt},
        "source": {
            "repository": DEFAULT_REPOSITORY,
            "ref": DEFAULT_REF,
        },
        "target": {
            "autoCreatePr": False,
        },
    }
    if branch_name:
        payload["target"]["branchName"] = branch_name
    response = cursor_request("/agents", payload, method="POST")
    agent_id = response.get("id")
    if not agent_id:
        raise CursorApiError("Launch agent response missing 'id'.")
    return agent_id


def wait_for_agent(agent_id: str, timeout: int, poll_interval: int) -> Dict[str, Any]:
    deadline = time.monotonic() + timeout
    last_status = None
    while time.monotonic() < deadline:
        status_payload = cursor_request(f"/agents/{agent_id}")
        last_status = status_payload.get("status")
        if last_status in {"FINISHED", "FAILED", "ERROR"}:
            return status_payload
        time.sleep(poll_interval)
    raise CursorApiError(f"Timed out waiting for agent {agent_id} (last status={last_status}).")


def fetch_agent_markdown(agent_id: str) -> Optional[str]:
    conversation = cursor_request(f"/agents/{agent_id}/conversation")
    messages = conversation.get("messages", [])
    for msg in reversed(messages):
        if msg.get("type") == "assistant_message":
            text = msg.get("text", "").strip()
            if text:
                return text
    return None


def heuristic_fallback(transcript: str, metadata: Dict[str, str]) -> str:
    lines = [line.strip() for line in transcript.splitlines() if line.strip()]
    excerpt = "\n".join(lines[: min(12, len(lines))])
    return textwrap.dedent(
        f"""
        _Cursor agent fallback summary_

        Meeting: {metadata['title']} ({metadata['date']})

        Transcript excerpt:
        {excerpt}
        """
    ).strip()


def build_output(
    content: str,
    metadata: Dict[str, str],
    transcript_path: pathlib.Path,
    agent_id: Optional[str],
) -> str:
    header = textwrap.dedent(
        f"""\
        ---
        meeting: "{metadata['title']}"
        date: "{metadata['date']}"
        source_transcript: "{transcript_path.as_posix()}"
        agent_id: "{agent_id or 'fallback'}"
        ---
        """
    ).strip()
    return f"{header}\n\n{content.strip()}\n"


def ensure_output_path(args: argparse.Namespace, slug: str) -> pathlib.Path:
    if args.output:
        return pathlib.Path(args.output)
    DEFAULT_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    return DEFAULT_OUTPUT_DIR / f"{slug}.md"


def main() -> None:
    args = parse_args()
    transcript_path = pathlib.Path(args.transcript)
    transcript_text = read_transcript(transcript_path)
    metadata = infer_metadata(transcript_path, args.meeting_date, args.meeting_title)
    slug = args.slug or slugify(transcript_path.stem)
    prompt = build_prompt(metadata, args.stakeholders, transcript_text)
    output_path = ensure_output_path(args, slug)

    agent_id: Optional[str] = None
    markdown: Optional[str] = None
    try:
        agent_id = launch_agent(prompt, args.branch_name)
        wait_for_agent(agent_id, args.timeout, args.poll_interval)
        markdown = fetch_agent_markdown(agent_id)
    except CursorApiError as exc:
        print(f"[warn] {exc}", file=sys.stderr)

    if not markdown:
        markdown = heuristic_fallback(transcript_text, metadata)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(build_output(markdown, metadata, transcript_path, agent_id), encoding="utf-8")
    print(f"Wrote meeting brief to {output_path}")


if __name__ == "__main__":
    main()
