# Meeting Summary Agent Specification

## Purpose
- Transform raw meeting transcripts into architect-ready markdown briefings.
- Extract business requirements, technical requirements, action items, next steps, recommended follow-up meetings (participants + agenda).
- Auto-generate Mermaid diagrams for business flows and solution/integration designs whenever those topics appear.

## Inputs
- **Transcript source**: Plain-text `.md` or `.txt` meeting notes committed under `meeting_transcripts/{yyyy-mm-dd}-{meeting-slug}.md`.
- **Metadata (optional)**:
  - `MEETING_TITLE`
  - `MEETING_DATE`
  - `STAKEHOLDERS`
- Script should infer metadata from filename when omitted.

## Prompt Blueprint
1. Provide meeting metadata and raw transcript.
2. Ask agent to:
   - Identify business requirements, technical requirements, constraints, assumptions.
   - Capture decisions, open questions, action items (assignee, due date if mentioned).
   - Recommend next meetings/workshops: purpose, target attendees, proposed agenda bullets.
   - Detect described flows:
     - Business/customer journey → output Mermaid `flowchart` or `sequence`.
     - Solution/integration discussions → output Mermaid `sequence` or `class` diagram referencing systems/interfaces.
   - Summarize key risks and dependencies.
3. Enforce output as a single markdown document with sections:
   - Summary
   - Business Requirements
   - Technical Requirements
   - Architecture / Integration Notes
   - Action Items
   - Next Steps & Upcoming Sessions
   - Mermaid Diagrams
   - Appendix (raw transcript reference link)

## Output Location & Naming
- Store generated files under `meeting_outputs/{yyyy-mm-dd}-{meeting-slug}.md`.
- Include front-matter header:
  ```
  ---
  meeting: "<title>"
  date: "<ISO date>"
  source_transcript: "meeting_transcripts/{file}"
  agent_id: "<cursor-agent-id>"
  ---
  ```

## Agent Configuration
- API: Cursor Cloud Agents `POST /v0/agents` (Launch an Agent) with Basic Auth API key.[^api]
- `source.repository`: `https://github.com/godhavari-gopal-covergo/architecture`, `ref`: `main`.
- `target.branchName`: allow script to pass `cursor/meeting-summary-{slug}` when automation needs agent-side branch (optional).
- On completion poll `/v0/agents/{id}` and `/v0/agents/{id}/conversation` to extract final markdown.

## Invocation Modes
1. **On-demand script**: Operator runs `python scripts/run_cursor_meeting_agent.py --transcript path`.
2. **GitHub workflow**: Triggered on pushes touching `meeting_transcripts/**`; calls script using stored Cursor API key secret, commits output, optionally opens PR.

## Success Criteria
- Markdown output consistently structured and checked into repo.
- Mermaid diagrams render (validated via `mmdc` or GitHub preview).
- Automation completes within GitHub Actions time limits (<10 minutes).
- Re-running agent for same transcript should overwrite previous output deterministically (unless `--append` specified).

[^api]: Cursor Cloud Agents API reference: [https://cursor.com/docs/cloud-agent/api/endpoints#launch-an-agent](https://cursor.com/docs/cloud-agent/api/endpoints#launch-an-agent).
