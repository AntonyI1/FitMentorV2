"""Exercise database - backward compatible wrapper around evidence-based database.

This module provides backward compatibility with the old exercise database
while using the new evidence-based exercise data internally.

The new database (exercise_data/) contains 120+ exercises with:
- Nippard tier rankings (S+ through D)
- Research citations and EMG data
- Detailed muscle head targeting
- Evidence-based programming notes

For new code, use exercise_query.py directly for full functionality.
"""

from .exercise_data import (
    ALL_EXERCISES as NEW_EXERCISES,
    get_all_exercises as _new_get_all,
    get_exercise_by_id as _new_get_by_id,
    get_exercises_by_muscle_group as _new_get_by_muscle,
    get_exercises_by_equipment as _new_get_by_equipment,
)

# Legacy exercise data - kept for backward compatibility with old integer IDs
# Maps old integer ID -> new string ID for lookup
LEGACY_ID_MAP = {
    1: "flat-barbell-bench-press",
    2: "flat-dumbbell-press",
    3: "incline-barbell-bench-press",
    4: "incline-dumbbell-press",
    5: "cable-crossover-mid",
    6: "flat-dumbbell-fly",
    7: "chest-dips",
    8: "push-ups-standard",
    9: "pull-ups",
    10: "lat-pulldown",
    11: "bent-over-row-wide",
    12: "single-arm-dumbbell-row",
    13: "seated-cable-row-close",
    14: "face-pulls-omni",
    15: "barbell-back-squat",
    16: "goblet-squat",
    17: "45-degree-leg-press",
    18: "romanian-deadlift",
    19: "romanian-deadlift",  # Dumbbell RDL maps to same
    20: "lying-leg-curl",
    21: "leg-extension",
    22: "walking-lunges-short",
    23: "bulgarian-split-squat",
    24: None,  # Calf raise not in new DB
    25: None,  # Bodyweight squat - use goblet squat
    26: "standing-barbell-overhead-press",
    27: "seated-dumbbell-overhead-press",
    28: "standing-dumbbell-lateral-raise",
    29: "bent-over-reverse-dumbbell-fly",
    30: "single-arm-cable-lateral-raise",
    31: "wide-grip-barbell-curl",
    32: "hammer-curl",
    33: "hammer-curl",
    34: "cable-pushdown-rope",
    35: "dumbbell-overhead-extension",
    36: "close-grip-bench-press",
    37: None,  # Plank - core not in new DB
    38: None,  # Cable crunch - core not in new DB
    39: "machine-chest-press",
    40: "decline-dumbbell-press",
    41: "pec-deck-machine",
    42: None,  # T-bar row maps to bent-over row
    43: "chest-supported-row-neutral",
    44: "straight-arm-pulldown",
    45: "inverted-row",
    46: "hack-squat",
    47: "good-mornings",
    48: "sissy-squat",
    49: "nordic-hamstring-curl",
    50: "barbell-hip-thrust",
    51: "glute-bridge",
    52: "cable-kickback",
    53: None,  # Sumo deadlift - use conventional
    54: None,  # DB hip thrust - use barbell
    55: "arnold-press",
    56: "machine-shoulder-press",
    57: "upright-row",
    58: "preacher-curl",
    59: "incline-dumbbell-curl",
    60: "wide-grip-cable-curl",
    61: "skull-crushers",
    62: "weighted-dips-upright",
    63: "cable-overhead-extension-rope",
    64: None,  # Hanging leg raise - core
    65: None,  # Ab wheel - core
    66: None,  # Decline sit-up - core
}

# Muscle group mapping: old names -> new names
MUSCLE_GROUP_MAP = {
    "chest": "chest",
    "back": "back",
    "legs": "legs",
    "glutes": "legs",  # Glutes are now under legs sub-region
    "shoulders": "shoulders",
    "biceps": "arms",
    "triceps": "arms",
    "core": None,  # Core not in new database
}

# Subcategory mapping: old names -> new sub_region names
SUBCATEGORY_MAP = {
    "mid_chest": "mid_chest",
    "upper_chest": "upper_chest",
    "lower_chest": "lower_chest",
    "lats": "lats",
    "mid_back": "upper_back",
    "rear_delt": "rear_delt",
    "quads": "quadriceps",
    "hamstrings": "hamstrings",
    "calves": None,  # No calves in new DB
    "glutes": "glutes",
    "front_delt": "front_delt",
    "side_delt": "side_delt",
    "biceps": "biceps_short_head",  # Default to short head
    "triceps": "triceps_lateral_medial",  # Default to lateral/medial
    "core": None,
}

# Difficulty mapping
DIFFICULTY_MAP = {
    "beginner": "easy",
    "intermediate": "medium",
    "advanced": "hard",
}


def _adapt_exercise(new_exercise):
    """Convert new exercise format to old format for backward compatibility."""
    # Reverse map sub_region to old subcategory
    subcategory = new_exercise["sub_region"]
    for old, new in SUBCATEGORY_MAP.items():
        if new == subcategory:
            subcategory = old
            break

    # Reverse map difficulty
    difficulty = new_exercise["difficulty"]
    for old, new in DIFFICULTY_MAP.items():
        if new == difficulty:
            difficulty = old
            break

    return {
        "id": new_exercise["id"],
        "name": new_exercise["name"],
        "muscle_group": new_exercise["muscle_group"],
        "subcategory": subcategory,
        "equipment": new_exercise["equipment"],
        "difficulty": difficulty,
        "type": new_exercise["type"],
        "category": new_exercise["type"],  # Use type as category
        "rest": new_exercise["rest"],
        # New fields available
        "nippard_tier": new_exercise.get("nippard_tier"),
        "research_notes": new_exercise.get("research_notes"),
        "targets": new_exercise.get("targets", []),
    }


# Build the EXERCISES list from new database for backward compatibility
EXERCISES = [_adapt_exercise(e) for e in NEW_EXERCISES]


def get_all_exercises():
    """Return all exercises in backward-compatible format."""
    return EXERCISES


def get_exercises_by_muscle_group(muscle_group):
    """Return exercises for a specific muscle group.

    Handles legacy muscle group names (biceps, triceps, glutes).
    """
    # Handle legacy muscle groups
    if muscle_group == "biceps":
        return [e for e in EXERCISES if e["muscle_group"] == "arms"
                and "biceps" in e.get("subcategory", "")]
    elif muscle_group == "triceps":
        return [e for e in EXERCISES if e["muscle_group"] == "arms"
                and "triceps" in e.get("subcategory", "")]
    elif muscle_group == "glutes":
        return [e for e in EXERCISES if e["muscle_group"] == "legs"
                and e.get("subcategory") == "glutes"]
    elif muscle_group == "core":
        # Core exercises not in new database
        return []

    return [e for e in EXERCISES if e["muscle_group"] == muscle_group]


def get_exercises_by_equipment(equipment_list):
    """Return exercises that can be performed with given equipment."""
    equipment_set = set(equipment_list)
    return [
        e for e in EXERCISES
        if set(e["equipment"]).issubset(equipment_set)
    ]


def get_exercise_by_id(exercise_id):
    """Return a specific exercise by ID.

    Supports both:
    - Legacy integer IDs (1-66)
    - New string IDs ("incline-barbell-bench-press")
    """
    # Try new string ID first
    if isinstance(exercise_id, str):
        new_exercise = _new_get_by_id(exercise_id)
        if new_exercise:
            return _adapt_exercise(new_exercise)
        return None

    # Try legacy integer ID
    if isinstance(exercise_id, int):
        new_id = LEGACY_ID_MAP.get(exercise_id)
        if new_id:
            new_exercise = _new_get_by_id(new_id)
            if new_exercise:
                return _adapt_exercise(new_exercise)
        return None

    return None


# Export new database functions for direct access
def get_evidence_based_exercises():
    """Return all exercises from the new evidence-based database."""
    return NEW_EXERCISES


def get_exercises_with_tier(min_tier="A"):
    """Return exercises with at least the specified Nippard tier."""
    from .exercise_data import TIER_RANK
    min_rank = TIER_RANK.get(min_tier, 0)
    return [
        e for e in NEW_EXERCISES
        if TIER_RANK.get(e.get("nippard_tier"), 0) >= min_rank
    ]
