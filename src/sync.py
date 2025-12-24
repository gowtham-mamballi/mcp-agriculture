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


def connect_db(db_path: str):
    """
    Create and return a SQLite connection.
    """
    pass


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
    Main sync entry point.
    """
    pass


if __name__ == "__main__":
    run()
