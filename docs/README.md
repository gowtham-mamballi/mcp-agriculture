# Google Sheet Template — MCP Agriculture v1

This document defines the **exact structure** of the Google Sheet used for
field data entry.

The Google Sheet is intentionally simple:
- No formulas
- No derived fields
- No logic
- Append-only rows

It acts only as a **data entry layer**.

---

## Sheet Name

MCP_Agriculture_v1

---

## Tab 1: Activities_Log

Used for day-to-day farm activities.

Columns (left to right):

- Date
- Crop
- Activity
- Done (checkbox)
- Labour_ManDays
- Labour_Cost_INR
- Input_Cost_INR
- Notes

Rules:
- One row = one real-world activity
- If nothing is done, no row is added
- Past rows should not be edited

---

## Tab 2: Harvest_Sales

Used for harvest and selling events.

Columns:

- Date
- Crop
- Quantity_Harvested
- Quantity_Sold
- Price_Per_Unit_INR
- Market
- Transport_Misc_INR
- Notes

Rules:
- Units must be consistent within a season
- One row = one harvest or sale event

---

## Tab 3: Observations

Optional free-form notes.

Columns:

- Date
- Crop (optional)
- Observation

Used for context MCP cannot auto-detect.
