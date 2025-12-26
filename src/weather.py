"""
MCP Agriculture
Weather module (v2.1)

Purpose:
- Fetch factual daily weather data for a given location
- Store raw daily facts in SQLite
- Support current + last-year backfill
- No rules
- No predictions
"""

import requests
import sqlite3
from datetime import date, timedelta
from pathlib import Path


DB_PATH = Path(__file__).resolve().parent.parent / "mcp_agriculture.db"


def fetch_weather_range(lat: float, lon: float, start: date, end: date):
    """
    Fetch daily weather for a given date range.
    Uses:
    - forecast endpoint for recent/current data
    - archive endpoint for historical data
    """

    base_url = "https://api.open-meteo.com/v1/forecast"

    # Use archive endpoint for historical data
    if end < date.today():
        base_url = "https://archive-api.open-meteo.com/v1/archive"

    url = (
        f"{base_url}"
        f"?latitude={lat}"
        f"&longitude={lon}"
        f"&start_date={start.isoformat()}"
        f"&end_date={end.isoformat()}"
        "&daily=temperature_2m_max,temperature_2m_min,precipitation_sum"
        "&timezone=auto"
    )

    response = requests.get(url, timeout=15)
    response.raise_for_status()
    data = response.json()

    daily = data.get("daily", {})
    dates = daily.get("time", [])

    weather_rows = []

    for idx, d in enumerate(dates):
        weather_rows.append({
            "date": d,
            "temp_max_c": daily["temperature_2m_max"][idx],
            "temp_min_c": daily["temperature_2m_min"][idx],
            "rain_mm": daily["precipitation_sum"][idx],
        })

    return weather_rows


def store_weather_rows(rows):
    """
    Store weather rows into SQLite.
    Idempotent by date.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for w in rows:
        cursor.execute("""
            INSERT OR IGNORE INTO weather_daily
            (date, temp_max_c, temp_min_c, rain_mm)
            VALUES (?, ?, ?, ?)
        """, (
            w["date"],
            w["temp_max_c"],
            w["temp_min_c"],
            w["rain_mm"],
        ))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    LAT = 12.099017
    LON = 77.078704

    today = date.today()

    # --- Current year: last 30 days ---
    start_current = today - timedelta(days=30)
    print(f"Backfilling current weather from {start_current} to {today}...")
    current_rows = fetch_weather_range(LAT, LON, start_current, today)
    store_weather_rows(current_rows)
    print(f"Stored {len(current_rows)} current-year days.")

    # --- Last year: same window ---
    start_last_year = start_current.replace(year=start_current.year - 1)
    end_last_year = today.replace(year=today.year - 1)

    print(f"Backfilling last-year weather from {start_last_year} to {end_last_year}...")
    last_year_rows = fetch_weather_range(LAT, LON, start_last_year, end_last_year)
    store_weather_rows(last_year_rows)
    print(f"Stored {len(last_year_rows)} last-year days.")
