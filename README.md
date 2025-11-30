# architecture

## Meeting transcript → architecture brief automation

The repository contains a meeting-summary agent specification (`docs/meeting-agent.md`), an on-demand runner (`scripts/run_cursor_meeting_agent.py`), and a GitHub Actions workflow (`.github/workflows/cursor-meeting-summary.yml`) that translates raw meeting transcripts into architecture-ready markdown stored under `meeting_outputs/`.

### How it works

1. Commit transcripts (Markdown, text, or exported `.docx`) under `meeting_transcripts/` (or the legacy folders listed in `scripts/list_changed_transcripts.py`).
2. The runner script reads each transcript, dispatches a Cursor Cloud Agent run via [`POST /v0/agents`](https://cursor.com/docs/cloud-agent/api/endpoints#launch-an-agent), and waits for the response conversation.
3. The resulting markdown document captures business + technical requirements, action items, next steps, and automatically includes Mermaid diagrams when the transcript mentions flows or integrations.
4. The GitHub workflow watches the transcript directories, invokes the runner for newly changed files, commits the generated briefs to `meeting_outputs/`, and also uploads them as workflow artifacts for convenience.

> ℹ️ `.gdoc` files are Drive pointers. Please export them to `.docx`/Markdown before committing; the runner prints a warning otherwise.

### One-time setup

1. Create a Cursor Cloud API key from the Cursor dashboard.
2. Save the key as the `CURSOR_API_KEY` repository secret (used by the workflow). Optional overrides:
   - `CURSOR_API_BASE` – alternate Cursor API host.
   - `CURSOR_REPOSITORY` / `CURSOR_REPOSITORY_REF` – override repo metadata sent to the agent.
   - `CURSOR_SKIP_SSL_VERIFY=1` – disable TLS validation when debugging.
3. Optionally customise the prompt/sections in `docs/meeting-agent.md` and the runner script.

### Running the agent locally / on demand

```
python scripts/run_cursor_meeting_agent.py \
  --transcript meeting_transcripts/2025-11-29-onboarding.md \
  --meeting-title "Onboarding Workshop" \
  --stakeholders "Product, Engineering, Security"
```

Outputs land in `meeting_outputs/<slug>.md` by default; use `--output` to override.

### GitHub Actions automation

- Trigger: push events touching `meeting-notes/**`, `docs/meeting-notes/**`, `transcripts/**`, or `meeting_transcripts/**`.
- Workflow steps:
  1. Detect changed transcripts (`scripts/list_changed_transcripts.py`).
  2. For each file, run `scripts/run_cursor_meeting_agent.py`.
  3. Commit any new/updated files under `meeting_outputs/`.
  4. Upload the folder as the `cursor-meeting-briefs` artifact.

Download artifacts for quick review, or browse committed briefs directly in the repository history. Use the runner script manually for ad-hoc transcripts outside of GitHub.
