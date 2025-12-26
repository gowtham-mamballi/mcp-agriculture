# MCP Agriculture – Weather Integration (V2.1)

This document describes the weather capabilities added on top of MCP Agriculture v1.
All functionality described here is **factual and non-advisory by design**.

---

## Why weather was added

Weather was introduced to MCP to:
- provide environmental context to farm activities
- enable explainable, data-backed reasoning later
- avoid intuition-driven or calendar-only decisions

Weather data is treated as **truth input**, not intelligence.

---

## Location

All weather data is tied to a fixed farm location:

- Latitude: 12.099017
- Longitude: 77.078704

This location is intentionally explicit and frozen.

---

## Data source

Weather data is sourced from **Open-Meteo**:
- Free
- No API key
- Research-grade
- Transparent endpoints

Two endpoints are used deliberately:

- `/v1/forecast` → current & near-term data
- `/v1/archive` → historical data (previous years)

This separation prevents silent data errors.

---

## What data is collected

### Daily weather facts

Stored in SQLite table `weather_daily`:

- date
- max temperature (°C)
- min temperature (°C)
- rainfall (mm)

Each date is stored **once** (idempotent).

---

## Historical backfill

The system currently backfills:

- Last 30 days (current year)
- Same 30-day window, last year

This provides short-term historical context without assuming long-term normals.

---

## Derived (computed) facts

Derived facts are computed **at runtime**, not persisted yet:

- days since sowing
- days since last rain
- cumulative rainfall in first 14 days after sowing

These are **numbers only**, not signals.

---

## Year-over-year comparison

The system supports comparison of:

- Same calendar window (e.g., last 30 days)
- Current year vs previous year
- Output includes:
  - total rainfall (mm)
  - delta (mm)
  - percentage change

### Important clarification

This comparison:
- does NOT represent annual rainfall
- does NOT imply crop stress
- does NOT generate alerts or advice

It is a **calendar-window comparison only**.

Interpretation must always include crop stage and context.

---

## What this system deliberately does NOT do (yet)

- No irrigation advice
- No drought declaration
- No crop recommendations
- No automatic rules based on weather
- No predictive models

All of the above are consciously deferred.

---

## Design philosophy

Weather integration follows these rules:

- facts before signals
- signals before rules
- rules before advice
- advice only when explainable

This keeps MCP auditable and trustworthy.

---

## Current status

- MCP Agriculture v1: complete
- Weather integration (v2.1 foundation): complete
- System is stable on macOS and Windows

Further work will build on this documented base.
