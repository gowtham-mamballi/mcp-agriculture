"""
MCP Agriculture
Weather comparison (v2.1)

Purpose:
- Compare rainfall this year vs last year for the same window
- Facts only
- No rules
- No persistence
"""

import sqlite3
from datetime import date, timedelta
from pathlib import Path


DB_PATH = Path(__file__).resolve().parent.parent / "mcp_agriculture.db"


def get_rain_sum(start_date: str, end_date: str) -> float:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(rain_mm)
        FROM weather_daily
        WHERE date BETWEEN ? AND ?
    """, (start_date, end_date))

    result = cursor.fetchone()[0]
    conn.close()

    return result or 0.0


def compare_rainfall(days: int = 30):
    today = date.today()
    start_current = today - timedelta(days=days)

    start_last_year = start_current.replace(year=start_current.year - 1)
    end_last_year = today.replace(year=today.year - 1)

    rain_current = get_rain_sum(
        start_current.isoformat(),
        today.isoformat()
    )

    rain_last_year = get_rain_sum(
        start_last_year.isoformat(),
        end_last_year.isoformat()
    )

    delta = rain_current - rain_last_year
    pct_change = None

    if rain_last_year > 0:
        pct_change = (delta / rain_last_year) * 100

    print("\nRainfall comparison (facts only)")
    print("--------------------------------")
    print(f"Window (days): {days}")
    print(f"Current year rain (mm): {round(rain_current, 2)}")
    print(f"Last year rain (mm):    {round(rain_last_year, 2)}")
    print(f"Delta (mm):             {round(delta, 2)}")

    if pct_change is not None:
        print(f"Change (%):             {round(pct_change, 1)}%")
    else:
        print("Change (%):             N/A (no rain last year)")


if __name__ == "__main__":
    compare_rainfall(days=30)
