"""
MCP Agriculture
Weather ↔ Crop linking (v2.1)

Purpose:
- Derive factual metrics linking weather to crops
- NO rules
- NO alerts
- NO recommendations
"""

import sqlite3
from datetime import date, datetime
from pathlib import Path


DB_PATH = Path(__file__).resolve().parent.parent / "mcp_agriculture.db"


def get_crops(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT crop_id, crop_name, sowing_date
        FROM crops
    """)
    return cursor.fetchall()


def get_weather_since(conn, start_date: str):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT date, rain_mm
        FROM weather_daily
        WHERE date >= ?
        ORDER BY date ASC
    """, (start_date,))
    return cursor.fetchall()


def derive_crop_weather_facts():
    conn = sqlite3.connect(DB_PATH)

    today = date.today()

    crops = get_crops(conn)

    if not crops:
        print("No crops found.")
        return

    for crop_id, crop_name, sowing_date in crops:
        sow_date = datetime.strptime(sowing_date, "%Y-%m-%d").date()
        days_since_sowing = (today - sow_date).days

        weather = get_weather_since(conn, sowing_date)

        days_since_last_rain = None
        rain_first_14_days = 0.0

        for d, rain in weather:
            w_date = datetime.strptime(d, "%Y-%m-%d").date()

            if rain and rain > 0:
                days_since_last_rain = (today - w_date).days

            if (w_date - sow_date).days < 14:
                rain_first_14_days += rain or 0

        print(f"\nCrop: {crop_name}")
        print(f"  Days since sowing: {days_since_sowing}")
        print(f"  Days since last rain: {days_since_last_rain}")
        print(f"  Rain in first 14 days (mm): {round(rain_first_14_days, 2)}")

    conn.close()


if __name__ == "__main__":
    derive_crop_weather_facts()
