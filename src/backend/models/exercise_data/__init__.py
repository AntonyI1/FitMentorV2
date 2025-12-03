"""Evidence-based exercise database with 100+ exercises.

Source: Jeff Nippard's evidence-based recommendations and EMG research.
"""

from .chest import CHEST_EXERCISES
from .arms import ARM_EXERCISES
from .shoulders import SHOULDER_EXERCISES
from .back import BACK_EXERCISES
from .legs import LEG_EXERCISES

# Constants
MUSCLE_GROUPS = ["chest", "arms", "shoulders", "back", "legs"]

SUB_REGIONS = {
    "chest": ["upper_chest", "mid_chest", "lower_chest"],
    "arms": ["biceps_short_head", "biceps_long_head", "triceps_lateral_medial", "triceps_long_head"],
    "shoulders": ["front_delt", "side_delt", "rear_delt"],
    "back": ["upper_back", "lats", "lower_back"],
    "legs": ["quadriceps", "hamstrings", "glutes"]
}

EQUIPMENT = [
    "bodyweight", "dumbbell", "barbell", "barbell_ez",
    "bench", "rack", "cable", "machine", "pullup_bar"
]

DIFFICULTIES = ["easy", "medium", "hard"]
DIFFICULTY_RANK = {"easy": 1, "medium": 2, "hard": 3}

NIPPARD_TIERS = ["S+", "S", "A+", "A", "B+", "B", "C", "D"]
TIER_RANK = {"S+": 8, "S": 7, "A+": 6, "A": 5, "B+": 4, "B": 3, "C": 2, "D": 1, None: 0}

# Aggregate all exercises
ALL_EXERCISES = (
    CHEST_EXERCISES +
    ARM_EXERCISES +
    SHOULDER_EXERCISES +
    BACK_EXERCISES +
    LEG_EXERCISES
)

# Build lookup by ID
_EXERCISE_BY_ID = {e["id"]: e for e in ALL_EXERCISES}


def get_all_exercises():
    """Return all exercises."""
    return ALL_EXERCISES


def get_exercise_by_id(exercise_id):
    """Return a specific exercise by ID (string slug)."""
    return _EXERCISE_BY_ID.get(exercise_id)


def get_exercises_by_muscle_group(muscle_group):
    """Return exercises for a specific muscle group."""
    return [e for e in ALL_EXERCISES if e["muscle_group"] == muscle_group]


def get_exercises_by_sub_region(sub_region):
    """Return exercises for a specific sub-region."""
    return [e for e in ALL_EXERCISES if e["sub_region"] == sub_region]


def get_exercises_by_equipment(equipment_list):
    """Return exercises that can be performed with given equipment."""
    equipment_set = set(equipment_list)
    return [
        e for e in ALL_EXERCISES
        if set(e["equipment"]).issubset(equipment_set)
    ]


def get_exercises_by_difficulty(max_difficulty):
    """Return exercises up to and including the given difficulty."""
    max_rank = DIFFICULTY_RANK.get(max_difficulty, 3)
    return [
        e for e in ALL_EXERCISES
        if DIFFICULTY_RANK.get(e["difficulty"], 1) <= max_rank
    ]


def get_exercises_by_tier(min_tier):
    """Return exercises with tier >= min_tier."""
    min_rank = TIER_RANK.get(min_tier, 0)
    return [
        e for e in ALL_EXERCISES
        if TIER_RANK.get(e.get("nippard_tier"), 0) >= min_rank
    ]
