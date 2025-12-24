"""
MCP Agriculture v1
Sync module

Purpose:
- Initialize SQLite database using canonical schema
- Read data from Google Sheets (field input) — DRY RUN ONLY
- Print row counts to verify connectivity

No business logic lives here.
No rules are applied here.
"""

import json
import sqlite3
from pathlib import Path
from typing import Optional


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


def run():
    """
    Minimal runnable entry point.
    - Initializes DB using schema
    - Inserts demo season (once)
    - Performs Google Sheet dry-run read
    """

    # --- Load config (local only, never committed) ---
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    # --- Initialize database ---
    db_path = "mcp_agriculture.db"
    conn = connect_db(db_path)
    cursor = conn.cursor()

    schema_path = Path(__file__).resolve().parent.parent / "schema" / "mcp_agriculture.sql"
    with open(schema_path, "r", encoding="utf-8") as f:
        schema_sql = f.read()

    cursor.executescript(schema_sql)

    # Insert demo season only if empty
    cursor.execute("SELECT COUNT(*) FROM seasons;")
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.execute("""
            INSERT INTO seasons (name, start_date, status, notes)
            VALUES (?, ?, ?, ?);
        """, ("Demo Season", "2025-01-01", "active", "Initial test run"))

    conn.commit()
    conn.close()

    # --- DRY RUN: Read Google Sheet ---
    dry_run_read_sheet(config["google_sheet_id"])

    print("MCP Agriculture v1: database initialized using schema.")


if __name__ == "__main__":
    run()
