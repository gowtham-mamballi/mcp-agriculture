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


def evaluate_season(season_id: int) -> List[CropStatus]:
    """
    Evaluate all crops in a season.
    """
    pass
