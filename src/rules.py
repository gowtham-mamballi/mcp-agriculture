"""
MCP Agriculture v1
Rules engine

Purpose:
- Apply frozen crop timelines
- Detect missed or delayed activities
- Assign simple status per crop:
  - ON_TRACK
  - WATCH
  - ACTION_NEEDED

This module contains NO data ingestion logic.
This module contains NO pricing or prediction logic.
"""

from enum import Enum
from typing import List
import sqlite3
from pathlib import Path


class CropStatus(Enum):
    ON_TRACK = "on_track"
    WATCH = "watch"
    ACTION_NEEDED = "action_needed"


def load_timelines():
    """
    Load standard, frozen crop timelines.
    Implementation deferred.
    """
    pass

def evaluate_crop(crop, activities, timeline=None) -> CropStatus:
    """
    Very first rule (v1):
    - If no completed weeding activity exists -> WATCH
    - Else -> ON_TRACK
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

    activities = []
    for activity_type, done in rows:
        activities.append({
            "activity_type": activity_type,
            "done": done
        })

    return activities
  
if __name__ == "__main__":
    db_path = Path(__file__).resolve().parent.parent / "mcp_agriculture.db"

    # TEMP: assume crop_id = 1 for now
    crop_id = 1

    activities = get_activities_for_crop(str(db_path), crop_id)
    status = evaluate_crop(crop=None, activities=activities)

    print(f"Crop {crop_id} status:", status.value)

