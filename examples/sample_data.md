# Sample Data — MCP Agriculture v1

This file shows **example records** to help understand how data flows
through MCP Agriculture.

This is NOT executable data.
This is NOT meant to be imported directly.

---

## Season

| name        | start_date | end_date | status |
|-------------|------------|----------|--------|
| Kharif 2025 | 2025-06-01 |          | active |

---

## Crops

| crop_name  | area_acres | sowing_date |
|------------|------------|-------------|
| Ragi       | 0.5        | 2025-06-05  |
| Groundnut  | 0.5        | 2025-06-07  |

---

## Activities

| activity_date | crop       | activity_type | done | labour_mandays | labour_cost_inr | input_cost_inr |
|---------------|------------|---------------|------|----------------|-----------------|----------------|
| 2025-06-05    | Ragi       | sowing        | 1    | 2              | 800             | 300            |
| 2025-06-25    | Ragi       | weeding       | 1    | 1              | 400             | 0              |
| 2025-06-07    | Groundnut  | sowing        | 1    | 3              | 1200            | 900            |

---

## Harvest & Sales

| event_date | crop       | quantity_harvested | quantity_sold | price_per_unit_inr | market |
|------------|------------|--------------------|---------------|--------------------|--------|
| 2025-09-20 | Ragi       | 450                | 450           | 3200               | APMC   |
