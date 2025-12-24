"""
MCP Agriculture v1
Rules engine

Purpose:
- Detect missed or delayed activities
- Assign simple status per crop:
  - ON_TRACK
  - WATCH
  - ACTION_NEEDED (future)

This module contains NO data ingestion logic.
This module contains NO pricing or prediction logic.
"""

from enum import Enum
import sqlite3
from pathlib import Path


class CropStatus(Enum):
    ON_TRACK = "on_track"
    WATCH = "watch"
    ACTION_NEEDED = "action_needed"


def evaluate_crop(crop, activities, timeline=None) -> CropStatus:
    """
    v1 rule:
    - If at least one completed weeding activity exists -> ON_TRACK
    - Else -> WATCH
    """
    for activity in activities:
        if (
            activity.get("activity_type") == "weeding"
            and activity.get("done") == 1
        ):
            return CropStatus.ON_TRACK

    return CropStatus.WATCH


def get_activities_for_crop(db_path: str, crop_id: int):
    """
    Read activities for a crop from SQLite.
    Returns a list of dicts compatible with evaluate_crop().
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT activity_type, done
        FROM activities
        WHERE crop_id = ?
    """, (crop_id,))

    rows = cursor.fetchall()
    conn.close()

    return [
        {"activity_type": activity_type, "done": done}
        for activity_type, done in rows
    ]


def get_all_crop_ids(db_path: str):
    """
    Fetch all crop_ids from SQLite.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT crop_id FROM crops;")
    rows = cursor.fetchall()
    conn.close()

    return [r[0] for r in rows]


if __name__ == "__main__":
    db_path = Path(__file__).resolve().parent.parent / "mcp_agriculture.db"

    crop_ids = get_all_crop_ids(str(db_path))

    if not crop_ids:
        print("No crops found.")
    else:
        for crop_id in crop_ids:
            activities = get_activities_for_crop(str(db_path), crop_id)
            status = evaluate_crop(crop=None, activities=activities)
            print(f"Crop {crop_id} status: {status.value}")
