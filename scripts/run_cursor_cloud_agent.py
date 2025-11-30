#!/usr/bin/env python3
"""
Simple helper that feeds a transcript into a Cursor Cloud agent (or falls back
to a lightweight heuristic summary) and writes the resulting markdown file.

The goal is to let GitHub Actions call a single script without duplicating the
Cursor-specific integration and transcript parsing logic.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import re
import sys
import textwrap
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
import zipfile
from typing import Optional


NAMESPACE = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a Cursor Cloud agent on a transcript.")
    parser.add_argument("--input", required=True, help="Path to the transcript file.")
    parser.add_argument("--output", required=True, help="Destination markdown file.")
    parser.add_argument(
        "--prompt",
        default="Provide an architecture-focused summary of the key technical decisions, rationale, and open issues.",
        help="Instruction that gets passed alongside the transcript.",
    )
    return parser.parse_args()


def extract_text(path: pathlib.Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".docx":
        return extract_docx_text(path)
    if suffix in {".md", ".txt"}:
        return path.read_text(encoding="utf-8")
    if suffix == ".gdoc":
        data = json.loads(path.read_text(encoding="utf-8"))
        url = data.get("url", "https://docs.google.com/")
        message = (
            "Google .gdoc files are pointers and do not include the transcript text. "
            "Export the document as Markdown or DOCX and commit that file instead.\n\n"
            f"Referenced document: {url}"
        )
        return message
    # Fall back to binary-safe read and decode errors.
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


def call_cursor_cloud_agent(transcript: str, prompt: str, source_path: pathlib.Path) -> Optional[str]:
    """
    Attempt to invoke a Cursor Cloud agent via HTTP.

    The actual URL and payload format can be adjusted by setting the following
    environment variables inside the GitHub Action:

      * CURSOR_AGENT_URL  - Fully qualified endpoint for the agent run.
      * CURSOR_AGENT_ID   - Identifier of the agent/workflow to execute.
      * CURSOR_API_KEY    - Bearer token or API key used for auth.

    If any variable is missing, or if the HTTP request fails, the caller should
    fall back to a heuristic summary.
    """
    url = os.getenv("CURSOR_AGENT_URL")
    api_key = os.getenv("CURSOR_API_KEY")
    agent_id = os.getenv("CURSOR_AGENT_ID")

    if not (url and api_key and agent_id):
        return None

    payload = {
        "agent_id": agent_id,
        "input": {
            "prompt": prompt,
            "transcript": transcript,
            "source_path": str(source_path),
        },
    }
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            raw = response.read().decode("utf-8")
            parsed = json.loads(raw)
    except (urllib.error.URLError, ValueError, json.JSONDecodeError) as exc:
        print(f"[warn] Cursor Cloud agent call failed: {exc}", file=sys.stderr)
        return None

    for key in ("summary", "output", "output_markdown", "result"):
        value = parsed.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return None


def heuristic_summary(transcript: str, source_path: pathlib.Path, prompt: str) -> str:
    """
    Provide a very lightweight fallback summary so that the workflow still
    produces a file even when the Cursor Cloud agent cannot be reached yet.
    """
    lines = [line.strip() for line in transcript.splitlines() if line.strip()]
    excerpt = "\n".join(lines[: min(12, len(lines))])
    body = textwrap.dedent(
        f"""
        _Cursor Cloud agent fallback mode_

        Prompt: {prompt}

        Transcript excerpt:

        {excerpt}
        """
    ).strip()
    return body


def wrap_markdown(content: str, source_path: pathlib.Path) -> str:
    timestamp = dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    title = f"Architecture Summary – {source_path.stem}"
    header = textwrap.dedent(
        f"""\
        # {title}

        - Source file: `{source_path}`
        - Generated at: {timestamp}
        """
    )
    return f"{header}\n\n{content.strip()}\n"


def main() -> None:
    args = parse_args()
    input_path = pathlib.Path(args.input)
    output_path = pathlib.Path(args.output)
    text = extract_text(input_path)

    agent_output = call_cursor_cloud_agent(text, args.prompt, input_path)
    if agent_output:
        summary_body = agent_output
    else:
        summary_body = heuristic_summary(text, input_path, args.prompt)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(wrap_markdown(summary_body, input_path), encoding="utf-8")
    print(f"Wrote summary to {output_path}")


if __name__ == "__main__":
    main()
