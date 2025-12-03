"""Query interface for the evidence-based exercise database.

Provides filtering, ranking, and lookup functions for workout generation.
"""

from .exercise_data import (
    ALL_EXERCISES,
    MUSCLE_GROUPS,
    SUB_REGIONS,
    EQUIPMENT,
    DIFFICULTIES,
    DIFFICULTY_RANK,
    NIPPARD_TIERS,
    TIER_RANK,
    get_exercise_by_id,
    get_exercises_by_muscle_group,
    get_exercises_by_sub_region,
    get_exercises_by_equipment,
    get_exercises_by_difficulty,
    get_exercises_by_tier,
)


class ValidationError(Exception):
    """Raised when query parameters are invalid."""
    pass


def validate_muscle_group(muscle_group):
    """Validate muscle group parameter."""
    if muscle_group and muscle_group.lower() not in MUSCLE_GROUPS:
        raise ValidationError(
            f"Invalid muscle_group: {muscle_group}. "
            f"Valid options: {', '.join(MUSCLE_GROUPS)}"
        )


def validate_sub_region(sub_region):
    """Validate sub-region parameter."""
    all_sub_regions = [sr for srs in SUB_REGIONS.values() for sr in srs]
    if sub_region and sub_region.lower() not in all_sub_regions:
        raise ValidationError(
            f"Invalid sub_region: {sub_region}. "
            f"Valid options: {', '.join(all_sub_regions)}"
        )


def validate_equipment(equipment_list):
    """Validate equipment list."""
    if equipment_list:
        for eq in equipment_list:
            if eq.lower() not in EQUIPMENT:
                raise ValidationError(
                    f"Invalid equipment: {eq}. "
                    f"Valid options: {', '.join(EQUIPMENT)}"
                )


def validate_difficulty(difficulty):
    """Validate difficulty parameter."""
    if difficulty and difficulty.lower() not in DIFFICULTIES:
        raise ValidationError(
            f"Invalid difficulty: {difficulty}. "
            f"Valid options: {', '.join(DIFFICULTIES)}"
        )


def validate_tier(tier):
    """Validate tier parameter."""
    if tier and tier not in NIPPARD_TIERS:
        raise ValidationError(
            f"Invalid tier: {tier}. "
            f"Valid options: {', '.join(NIPPARD_TIERS)}"
        )


def query_exercises(
    muscle_group=None,
    sub_region=None,
    equipment=None,
    max_difficulty=None,
    min_tier=None,
    exercise_type=None,
    sort_by_tier=True
):
    """
    Query exercises with multiple filter criteria.

    Args:
        muscle_group: Filter by muscle group (chest, arms, shoulders, back, legs)
        sub_region: Filter by sub-region (upper_chest, biceps_long_head, etc.)
        equipment: List of available equipment - returns exercises possible with this set
        max_difficulty: Maximum difficulty level (easy, medium, hard)
        min_tier: Minimum Nippard tier (S+, S, A+, A, B+, B, C, D)
        exercise_type: compound or isolation
        sort_by_tier: If True, sort results by tier (highest first), then by name

    Returns:
        List of matching exercises
    """
    # Validate inputs
    validate_muscle_group(muscle_group)
    validate_sub_region(sub_region)
    validate_equipment(equipment)
    validate_difficulty(max_difficulty)
    validate_tier(min_tier)

    if exercise_type and exercise_type.lower() not in ["compound", "isolation"]:
        raise ValidationError(
            f"Invalid exercise_type: {exercise_type}. "
            f"Valid options: compound, isolation"
        )

    # Start with all exercises
    results = ALL_EXERCISES.copy()

    # Apply filters
    if muscle_group:
        results = [e for e in results if e["muscle_group"] == muscle_group.lower()]

    if sub_region:
        results = [e for e in results if e["sub_region"] == sub_region.lower()]

    if equipment:
        equipment_set = set(eq.lower() for eq in equipment)
        results = [
            e for e in results
            if set(e["equipment"]).issubset(equipment_set)
        ]

    if max_difficulty:
        max_rank = DIFFICULTY_RANK.get(max_difficulty.lower(), 3)
        results = [
            e for e in results
            if DIFFICULTY_RANK.get(e["difficulty"], 1) <= max_rank
        ]

    if min_tier:
        min_rank = TIER_RANK.get(min_tier, 0)
        results = [
            e for e in results
            if TIER_RANK.get(e.get("nippard_tier"), 0) >= min_rank
        ]

    if exercise_type:
        results = [e for e in results if e["type"] == exercise_type.lower()]

    # Sort by tier (highest first), then by name
    if sort_by_tier:
        results.sort(
            key=lambda e: (-TIER_RANK.get(e.get("nippard_tier"), 0), e["name"])
        )
    else:
        results.sort(key=lambda e: e["name"])

    return results


def get_top_exercises(muscle_group, n=5, exercise_type=None):
    """
    Get the top N exercises for a muscle group by Nippard tier.

    Args:
        muscle_group: The muscle group to query
        n: Number of exercises to return (default 5)
        exercise_type: Optional filter for compound or isolation

    Returns:
        List of top N exercises sorted by tier
    """
    return query_exercises(
        muscle_group=muscle_group,
        exercise_type=exercise_type,
        sort_by_tier=True
    )[:n]


def get_exercises_for_equipment_set(equipment_set, muscle_group=None):
    """
    Get all exercises possible with the given equipment.

    Args:
        equipment_set: List of available equipment
        muscle_group: Optional muscle group filter

    Returns:
        List of exercises that can be performed with given equipment
    """
    return query_exercises(
        muscle_group=muscle_group,
        equipment=equipment_set,
        sort_by_tier=True
    )


def get_compound_exercises(muscle_group=None, sub_region=None, min_tier=None):
    """
    Get compound exercises, optionally filtered.

    Args:
        muscle_group: Optional muscle group filter
        sub_region: Optional sub-region filter
        min_tier: Optional minimum tier filter

    Returns:
        List of compound exercises
    """
    return query_exercises(
        muscle_group=muscle_group,
        sub_region=sub_region,
        min_tier=min_tier,
        exercise_type="compound",
        sort_by_tier=True
    )


def get_isolation_exercises(muscle_group=None, sub_region=None, min_tier=None):
    """
    Get isolation exercises, optionally filtered.

    Args:
        muscle_group: Optional muscle group filter
        sub_region: Optional sub-region filter
        min_tier: Optional minimum tier filter

    Returns:
        List of isolation exercises
    """
    return query_exercises(
        muscle_group=muscle_group,
        sub_region=sub_region,
        min_tier=min_tier,
        exercise_type="isolation",
        sort_by_tier=True
    )


def get_exercises_by_sub_regions(sub_regions, equipment=None, max_difficulty=None):
    """
    Get exercises for multiple sub-regions at once.

    Args:
        sub_regions: List of sub-regions to query
        equipment: Optional equipment filter
        max_difficulty: Optional max difficulty filter

    Returns:
        Dict mapping sub_region -> list of exercises
    """
    result = {}
    for sr in sub_regions:
        result[sr] = query_exercises(
            sub_region=sr,
            equipment=equipment,
            max_difficulty=max_difficulty,
            sort_by_tier=True
        )
    return result


def get_substitutes(exercise_id, equipment=None):
    """
    Find substitute exercises that target the same sub-region.

    Args:
        exercise_id: The exercise to find substitutes for
        equipment: Optional equipment constraint

    Returns:
        List of substitute exercises (excluding the original)
    """
    exercise = get_exercise_by_id(exercise_id)
    if not exercise:
        return []

    subs = query_exercises(
        sub_region=exercise["sub_region"],
        equipment=equipment,
        exercise_type=exercise["type"],
        sort_by_tier=True
    )

    # Remove the original exercise
    return [e for e in subs if e["id"] != exercise_id]


# Equipment groupings for constraint-based workout generation
EQUIPMENT_PRESETS = {
    "bodyweight_only": ["bodyweight"],
    "home_basic": ["bodyweight", "dumbbell"],
    "home_full": ["bodyweight", "dumbbell", "bench", "pullup_bar"],
    "commercial_gym": [
        "bodyweight", "dumbbell", "barbell", "barbell_ez",
        "bench", "rack", "cable", "machine", "pullup_bar"
    ],
}


def get_exercises_for_preset(preset_name, muscle_group=None):
    """
    Get exercises available for a predefined equipment setup.

    Args:
        preset_name: One of bodyweight_only, home_basic, home_full, commercial_gym
        muscle_group: Optional muscle group filter

    Returns:
        List of exercises for the preset
    """
    equipment = EQUIPMENT_PRESETS.get(preset_name)
    if not equipment:
        raise ValidationError(
            f"Invalid preset: {preset_name}. "
            f"Valid options: {', '.join(EQUIPMENT_PRESETS.keys())}"
        )

    return get_exercises_for_equipment_set(equipment, muscle_group)
