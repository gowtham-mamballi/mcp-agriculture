"""
MCP Agriculture v1
Sync module

Purpose:
- Initialize SQLite database using canonical schema
- Read data from Google Sheets (field input)
- Sync Activities_Log into SQLite (idempotent, limited scope)

No business logic lives here.
No rules are applied here.
"""

import json
import sqlite3
from pathlib import Path


def connect_db(db_path: str):
    """
    Create and return a SQLite connection.
    """
    return sqlite3.connect(db_path)


def dry_run_read_sheet(sheet_id: str):
    """
    Read Activities_Log sheet and print row count.
    READ-ONLY dry run.
    """
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive.readonly"
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "credentials.json", scope
    )
    client = gspread.authorize(creds)

    sheet = client.open_by_key(sheet_id)
    worksheet = sheet.worksheet("Activities_Log")

    rows = worksheet.get_all_records()
    print(f"Activities_Log rows found: {len(rows)}")


def sync_activities_from_sheet(sheet_id: str, db_path: str):
    """
    Sync Activities_Log from Google Sheet into SQLite.
    Supports exactly TWO crops via explicit mapping.
    Idempotent inserts only.
    """

    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive.readonly"
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "credentials.json", scope
    )
    client = gspread.authorize(creds)

    sheet = client.open_by_key(sheet_id)
    worksheet = sheet.worksheet("Activities_Log")
    rows = worksheet.get_all_records()

    # Explicit crop mapping (LOCKED for this step)
    crop_map = {
        "Ragi": 1,
        "Groundnut": 2
    }

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    inserted = 0
    skipped = 0

    for row in rows:
        crop_name = row.get("Crop")
        crop_id = crop_map.get(crop_name)

        if not crop_id:
            print(f"SKIP: Unknown crop '{crop_name}'")
            skipped += 1
            continue

        activity_date = row.get("Date")
        activity_type = row.get("Activity")
        done = 1 if row.get("Done") else 0

        # Idempotency check
        cursor.execute("""
            SELECT 1 FROM activities
            WHERE crop_id = ?
              AND activity_date = ?
              AND activity_type = ?
        """, (crop_id, activity_date, activity_type))

        if cursor.fetchone():
            continue

        cursor.execute("""
            INSERT INTO activities (
                crop_id,
                activity_date,
                activity_type,
                done,
                labour_mandays,
                labour_cost_inr,
                input_cost_inr,
                notes
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            crop_id,
            activity_date,
            activity_type,
            done,
            row.get("Labour_ManDays"),
            row.get("Labour_Cost_INR"),
            row.get("Input_Cost_INR"),
            row.get("Notes")
        ))

        inserted += 1

    conn.commit()
    conn.close()

    print(f"Activities sync complete: {inserted} inserted, {skipped} skipped")


def run():
    """
    Entry point:
    - Initialize DB
    - Dry-run read Google Sheet
    - Real sync of Activities_Log
    """

    # Load local config
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    db_path = "mcp_agriculture.db"

    # Initialize DB using schema
    conn = connect_db(db_path)
    cursor = conn.cursor()

    schema_path = Path(__file__).resolve().parent.parent / "schema" / "mcp_agriculture.sql"
    with open(schema_path, "r", encoding="utf-8") as f:
        schema_sql = f.read()

    cursor.executescript(schema_sql)

    # Insert demo season only once
    cursor.execute("SELECT COUNT(*) FROM seasons;")
    if cursor.fetchone()[0] == 0:
        cursor.execute("""
            INSERT INTO seasons (name, start_date, status, notes)
            VALUES (?, ?, ?, ?);
        """, ("Demo Season", "2025-01-01", "active", "Initial test run"))

    conn.commit()
    conn.close()

    # Dry run read
    dry_run_read_sheet(config["google_sheet_id"])

    # Real activities sync
    sync_activities_from_sheet(
        config["google_sheet_id"],
        db_path
    )

    print("MCP Agriculture v1: sync run complete.")


if __name__ == "__main__":
    run()
