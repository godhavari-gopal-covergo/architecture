#!/usr/bin/env python3
"""
Utility script used by GitHub Actions to discover newly changed meeting
transcript files between two commits.

It prints one path per line so that downstream steps can iterate and feed each
file into the Cursor Cloud agent.
"""

from __future__ import annotations

import argparse
import pathlib
import subprocess
import sys
from typing import Iterable, List, Sequence

VALID_EXTENSIONS = {".gdoc", ".docx", ".md", ".txt"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="List meeting transcript files that changed between two commits."
    )
    parser.add_argument("base", help="Base commit SHA (can be all zeros for initial push).")
    parser.add_argument("head", help="Head commit SHA.")
    parser.add_argument(
        "--roots",
        nargs="*",
        default=["meeting-notes", "docs/meeting-notes", "transcripts", "meeting_transcripts"],
        help="Directory prefixes to scan for transcript files.",
    )
    return parser.parse_args()


def _run_git(args: Sequence[str]) -> List[str]:
    completed = subprocess.run(
        ["git", *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
        text=True,
    )
    return [line.strip() for line in completed.stdout.splitlines() if line.strip()]


def changed_files(base: str, head: str) -> Iterable[str]:
    zero = set("0")
    if set(base) == zero:
        # Initial push scenario: list entire tree at head.
        return _run_git(["ls-tree", "-r", "--name-only", head])
    return _run_git(["diff", "--name-only", f"{base}..{head}"])


def filter_transcripts(files: Iterable[str], roots: Sequence[str]) -> List[str]:
    root_prefixes = tuple(f"{root.rstrip('/')}/" for root in roots)
    matches: List[str] = []
    for path_str in files:
        path = pathlib.PurePosixPath(path_str)
        if root_prefixes and not path_str.startswith(root_prefixes):
            continue
        if path.suffix.lower() in VALID_EXTENSIONS:
            matches.append(path_str)
    return matches


def main() -> None:
    args = parse_args()
    try:
        files = changed_files(args.base, args.head)
    except subprocess.CalledProcessError as exc:
        sys.stderr.write(exc.stderr)
        sys.exit(exc.returncode)

   .filtered = filter_transcripts(files, args.roots)
    for path in filtered:
        print(path)


if __name__ == "__main__":
    main()
