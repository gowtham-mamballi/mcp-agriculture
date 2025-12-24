# MCP Agriculture

MCP Agriculture is a simple, open, field-first agriculture tracking system.

It is designed for small and medium farmers who want:
- clarity over memory
- records over guesswork
- learning over intuition

This is **not** a farming app.
This is **not** an AI prediction system.
This is a practical execution and learning framework.

---

## What this system does

- Tracks crops, activities, labour, costs, yield, and sales
- Uses standard crop timelines (frozen per season)
- Flags missed or delayed critical actions
- Builds a clean season-level record
- Learns from actual farm data over time

---

## What this system deliberately does NOT do

- No crop recommendations (yet)
- No yield or price prediction
- No per-plant or per-inch tracking
- No complex dashboards
- No SaaS or cloud lock-in

---

## How it works (high level)

1. **Google Sheets**  
   Used for live, mobile-friendly field data entry.

2. **SQLite**  
   Used as the system of record for truth, rules, and history.

3. **MCP Logic**  
   Reads data, applies timelines and rules, and produces status and summaries.

---

## Philosophy

- One step at a time
- No silent changes
- No overengineering
- Decisions once made are locked for v1

This system values **clarity over cleverness**.

---

## Repository structure (v1)

mcp-agriculture/
├── README.md
├── docs/
├── sheets/
├── schema/
├── src/
└── examples/


---

## Status

This repository is actively building **v1**.

Each step is committed and not revisited.
Future ideas go into v2.

---

## License

MIT License.

Local setup verified on Windows.
