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

...