-- MCP Agriculture v1
-- SQLite schema
-- This file defines the system-of-record database structure.
-- Tables are added incrementally and versioned.

PRAGMA foreign_keys = ON;
-- -------------------------------------------------
-- Table: seasons
-- -------------------------------------------------

CREATE TABLE IF NOT EXISTS seasons (
    season_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT,
    status TEXT NOT NULL CHECK (status IN ('active', 'closed')),
    notes TEXT
);

