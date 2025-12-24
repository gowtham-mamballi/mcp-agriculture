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

-- -------------------------------------------------
-- Table: activities
-- -------------------------------------------------

CREATE TABLE IF NOT EXISTS activities (
    activity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    crop_id INTEGER NOT NULL,
    activity_date TEXT NOT NULL,
    activity_type TEXT NOT NULL,
    done INTEGER NOT NULL CHECK (done IN (0, 1)),
    labour_mandays REAL,
    labour_cost_inr REAL,
    input_cost_inr REAL,
    notes TEXT,
    FOREIGN KEY (crop_id) REFERENCES crops(crop_id)
);

