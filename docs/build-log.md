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

