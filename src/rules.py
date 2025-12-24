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


def evaluate_crop(crop, activities, timeline) -> CropStatus:
    """
    Evaluate a single crop against its timeline.
    Returns CropStatus.
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

