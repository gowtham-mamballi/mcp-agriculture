# Google Sheet — MCP Agriculture v1

MCP Agriculture uses a **Google Sheet** for live, mobile-friendly field data entry.

The sheet is intentionally **not stored** in this repository.

Each user should create their **own copy** of the sheet using the
structure defined in:

docs/README.md

---

## How to use

1. Create a new Google Sheet
2. Name it exactly:

   MCP_Agriculture_v1

3. Create the following tabs (case-sensitive):
   - Activities_Log
   - Harvest_Sales
   - Observations

4. Add columns exactly as documented

---

## Important rules

- Do not add formulas
- Do not add calculated fields
- Do not change column names
- Append rows only

The Google Sheet is a **data entry layer only**.
All logic lives outside the sheet.
