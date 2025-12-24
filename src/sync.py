"""
MCP Agriculture v1
Sync module

Purpose:
- Read data from Google Sheets (field input)
- Validate rows
- Insert clean records into SQLite
- Idempotent: safe to run multiple times

No business logic lives here.
No rules are applied here.
"""

from typing import Optional
from pathlib import Path


def load_config():
    """
    Load configuration such as:
    - Google Sheet ID
    - SQLite DB path
    """
    pass


import sqlite3
def connect_db(db_path: str):
    """
    Create and return a SQLite connection.
    """
    conn = sqlite3.connect(db_path)
    return conn



def fetch_sheet_data():
    """
    Fetch raw rows from Google Sheets.
    Implementation intentionally deferred.
    """
    pass


def sync_seasons(rows):
    """
    Sync season records into the database.
    """
    pass


def sync_crops(rows):
    """
    Sync crop records into the database.
    """
    pass


def sync_activities(rows):
    """
    Sync activity records into the database.
    """
    pass


def sync_harvest_sales(rows):
    """
    Sync harvest and sales records into the database.
    """
    pass


def run():
    """
    Minimal runnable entry point.
    Creates a database using the canonical schema file.
    """
    db_path = "mcp_agriculture.db"
    conn = connect_db(db_path)
    cursor = conn.cursor()

    # Load and execute schema
    schema_path = Path(__file__).resolve().parent.parent / "schema" / "mcp_agriculture.sql"
    with open(schema_path, "r", encoding="utf-8") as f:
        schema_sql = f.read()

    cursor.executescript(schema_sql)

    # Insert one sample season if none exist
    cursor.execute("SELECT COUNT(*) FROM seasons;")
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.execute("""
            INSERT INTO seasons (name, start_date, status, notes)
            VALUES (?, ?, ?, ?);
        """, ("Demo Season", "2025-01-01", "active", "Initial test run"))

    conn.commit()
    conn.close()

    print("MCP Agriculture v1: database initialized using schema.")




if __name__ == "__main__":
    run()
