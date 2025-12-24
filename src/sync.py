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
    Creates a database and inserts one season.
    """
    db_path = "mcp_agriculture.db"
    conn = connect_db(db_path)
    cursor = conn.cursor()

    # Create seasons table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS seasons (
            season_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            start_date TEXT NOT NULL,
            end_date TEXT,
            status TEXT NOT NULL,
            notes TEXT
        );
    """)

    # Insert one sample season
    cursor.execute("""
        INSERT INTO seasons (name, start_date, status, notes)
        VALUES (?, ?, ?, ?);
    """, ("Demo Season", "2025-01-01", "active", "Initial test run"))

    conn.commit()
    conn.close()

    print("MCP Agriculture v1: database created and season inserted.")



if __name__ == "__main__":
    run()
