# MCP Agriculture v1 — Build Log

This document records the exact steps, commands, and milestones
achieved while building MCP Agriculture v1 on Windows.

The goal is reproducibility and clarity.

---

## Core principles (locked)

- Free forever (no fees, no subscriptions)
- Open-source, GitHub-hosted
- Google Sheets for field input
- SQLite as system of record
- Simple, explainable rules
- One step at a time, no silent changes

---

## Git setup (Windows)

Verified Git installation:

```bash
git --version

Configured identity:
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

Local workspace setup
mkdir projects
cd projects

Clone repository
git clone https://github.com/<username>/mcp-agriculture.git
cd mcp-agriculture

Verify
git status

Python verification (Windows)
py -V

First MCP run
py src/sync.py

Result:

SQLite DB created: mcp_agriculture.db
Schema loaded successfully

First rule added

Rule implemented:

If no completed weeding activity exists → status = WATCH
Else → status = ON_TRACK

Rules wired to real data
Run rules engine:
py src/rules.py
Status evaluated directly from SQLite.

Manual test — status flip
Inserted one weeding activity manually into SQLite.
Re-ran rules:
py src/rules.py
Observed result:
status: watch → on_track

Current state
MCP Agriculture v1 now has:
Persistent data storage (SQLite)
Real rule-based reasoning
Proven end-to-end execution loop
No paid services or dependencies
This document is updated incrementally as the system evolves.

--
---

## Google Sheet integration (read-only, v1)

MCP Agriculture uses Google Sheets as a **field-friendly input layer**.

At this stage, integration is intentionally **read-only**.

### Sheet details

- Sheet name: `MCP_Agriculture_v1`
- Tabs used:
  - `Activities_Log`
  - `Harvest_Sales`
  - `Observations`

### Authentication model

- Google Service Account
- Read-only access
- No user login required at runtime
- No billing enabled
- Credentials stored locally (`credentials.json`)
- Credentials are never committed to GitHub

### Verified behavior

The following command was executed successfully:

```bash
py src/sync.py

Activities_Log rows found: <N>
MCP Agriculture v1: database initialized using schema.

This confirms:

Google authentication works
Sheet access works
MCP can read real field data

Explicit non-goals (v1)
At this stage, MCP does NOT:
Write back to Google Sheets
Insert sheet data into SQLite automatically
Modify or validate sheet data
These capabilities are added incrementally in later steps.
