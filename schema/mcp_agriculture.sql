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

-- -------------------------------------------------
-- Table: crops
-- -------------------------------------------------

CREATE TABLE IF NOT EXISTS crops (
    crop_id INTEGER PRIMARY KEY AUTOINCREMENT,
    season_id INTEGER NOT NULL,
    crop_name TEXT NOT NULL,
    area_acres REAL NOT NULL,
    sowing_date TEXT,
    notes TEXT,
    FOREIGN KEY (season_id) REFERENCES seasons(season_id)
);
