"""Workout plan generator based on user parameters and training principles.

This module generates evidence-based workout plans with:
- Intelligent exercise selection ensuring muscle head coverage
- Movement pattern redundancy prevention
- Tier-prioritized exercise selection (S+ > S > A+ > A > ...)
- Experience-appropriate difficulty filtering
"""

from .workout_generator import ExerciseSelector, validate_workout, WORKOUT_CONSTRAINTS
from .exercise_data import TIER_RANK
from .movement_patterns import get_movement_pattern

VALID_GENDERS = {"male", "female"}
VALID_GOALS = {"strength", "hypertrophy", "endurance", "weight_loss"}
VALID_EXPERIENCE = {"beginner", "intermediate", "advanced"}
VALID_EQUIPMENT = {
    "barbell", "dumbbell", "machine", "cable", "bench",
    "rack", "pullup_bar", "bodyweight", "barbell_ez"
}

GOAL_PARAMS = {
    "strength": {"reps": "3-6", "sets": 4, "rest": 180, "rir": 1},
    "hypertrophy": {"reps": "8-12", "sets": 3, "rest": 120, "rir": 1},
    "endurance": {"reps": "15-20", "sets": 3, "rest": 60, "rir": 2},
    "weight_loss": {"reps": "12-15", "sets": 3, "rest": 60, "rir": 1},
}

EXPERIENCE_MULTIPLIERS = {
    "beginner": 0.85,
    "intermediate": 1.0,
    "advanced": 1.15,
}

# Gender-specific volume adjustments
# Females: significantly more focus on legs/glutes, less on upper body pushing
GENDER_VOLUME_ADJUSTMENTS = {
    "male": {
        "legs": 1.0,
        "chest": 1.0,
        "back": 1.0,
        "shoulders": 1.0,
        "arms": 1.0,
    },
    "female": {
        "legs": 2.0,  # Double leg exercises for females
        "chest": 0.5,  # Half the chest volume
        "back": 1.0,  # Back remains important for posture
        "shoulders": 0.5,  # Half the shoulder volume
        "arms": 0.5,  # Half the arm volume
    },
}

# Maximum exercises per workout by gender (females cap lower on push days)
GENDER_MAX_EXERCISES = {
    "male": {"push": 9, "pull": 9, "legs": 9, "upper": 9, "lower": 9, "full_body": 9},
    "female": {"push": 6, "pull": 8, "legs": 9, "upper": 8, "lower": 9, "full_body": 9},
}

# Sub-regions to exclude by gender
GENDER_EXCLUDED_SUBREGIONS = {
    "male": ["glutes"],  # Males don't do dedicated glute work
    "female": [],
}

# Split configurations with split_type for intelligent sub-region targeting
# variant: identifies A/B/C variants of the same workout type
# variant_group: groups days that should share top-tier exercises but differ in accessories
SPLITS = {
    3: {
        "name": "Full Body 3x/week",
        "days": [
            {
                "name": "Full Body A",
                "split_type": "full_body",
                "variant": "A",
                "variant_group": "full_body",
                "muscle_groups": ["chest", "back", "legs", "shoulders", "arms"],
            },
            {
                "name": "Full Body B",
                "split_type": "full_body",
                "variant": "B",
                "variant_group": "full_body",
                "muscle_groups": ["chest", "back", "legs", "shoulders", "arms"],
            },
            {
                "name": "Full Body C",
                "split_type": "full_body",
                "variant": "C",
                "variant_group": "full_body",
                "muscle_groups": ["chest", "back", "legs", "shoulders", "arms"],
            },
        ],
    },
    4: {
        "name": "Upper/Lower 4x/week",
        "days": [
            {
                "name": "Upper A",
                "split_type": "upper",
                "variant": "A",
                "variant_group": "upper",
                "muscle_groups": ["chest", "back", "shoulders", "arms"],
            },
            {
                "name": "Lower A",
                "split_type": "legs",
                "variant": "A",
                "variant_group": "lower",
                "muscle_groups": ["legs"],
            },
            {
                "name": "Upper B",
                "split_type": "upper",
                "variant": "B",
                "variant_group": "upper",
                "muscle_groups": ["chest", "back", "shoulders", "arms"],
            },
            {
                "name": "Lower B",
                "split_type": "legs",
                "variant": "B",
                "variant_group": "lower",
                "muscle_groups": ["legs"],
            },
        ],
    },
    5: {
        "name": "Push/Pull/Legs 5x/week",
        "days": [
            {
                "name": "Push",
                "split_type": "push",
                "muscle_groups": ["chest", "shoulders", "arms"],
            },
            {
                "name": "Pull",
                "split_type": "pull",
                "muscle_groups": ["back", "arms"],
            },
            {
                "name": "Legs",
                "split_type": "legs",
                "muscle_groups": ["legs"],
            },
            {
                "name": "Upper",
                "split_type": "upper",
                "muscle_groups": ["chest", "back", "shoulders", "arms"],
            },
            {
                "name": "Lower",
                "split_type": "legs",
                "muscle_groups": ["legs"],
            },
        ],
    },
    6: {
        "name": "Push/Pull/Legs 6x/week",
        "days": [
            {
                "name": "Push A",
                "split_type": "push",
                "variant": "A",
                "variant_group": "push",
                "muscle_groups": ["chest", "shoulders", "arms"],
            },
            {
                "name": "Pull A",
                "split_type": "pull",
                "variant": "A",
                "variant_group": "pull",
                "muscle_groups": ["back", "arms"],
            },
            {
                "name": "Legs A",
                "split_type": "legs",
                "variant": "A",
                "variant_group": "legs",
                "muscle_groups": ["legs"],
            },
            {
                "name": "Push B",
                "split_type": "push",
                "variant": "B",
                "variant_group": "push",
                "muscle_groups": ["chest", "shoulders", "arms"],
            },
            {
                "name": "Pull B",
                "split_type": "pull",
                "variant": "B",
                "variant_group": "pull",
                "muscle_groups": ["back", "arms"],
            },
            {
                "name": "Legs B",
                "split_type": "legs",
                "variant": "B",
                "variant_group": "legs",
                "muscle_groups": ["legs"],
            },
        ],
    },
}

# Sub-region targeting based on split type
SPLIT_SUBREGIONS = {
    "push": {
        "chest": ["upper_chest", "mid_chest", "lower_chest"],
        "shoulders": ["front_delt", "side_delt"],
        "arms": ["triceps_lateral_medial", "triceps_long_head"],
    },
    "pull": {
        "back": ["upper_back", "lats"],
        "shoulders": ["rear_delt"],
        "arms": ["biceps_short_head", "biceps_long_head"],
    },
    "legs": {
        "legs": ["quadriceps", "hamstrings", "glutes"],
        "back": ["lower_back"],
    },
    "upper": {
        "chest": ["upper_chest", "mid_chest"],
        "back": ["upper_back", "lats"],
        "shoulders": ["front_delt", "side_delt", "rear_delt"],
        "arms": ["biceps_long_head", "triceps_long_head"],
    },
    "full_body": {
        "chest": ["mid_chest", "upper_chest"],
        "back": ["lats", "upper_back"],
        "shoulders": ["side_delt"],
        "arms": ["biceps_long_head", "triceps_long_head"],
        "legs": ["quadriceps", "glutes"],
    },
}

PROGRESSIONS = {
    "strength": {
        "method": "Linear Progression",
        "increment": "Add 2.5-5 lbs when you complete all sets at target reps",
        "deload": "Reduce weight by 10% after 3 failed sessions",
    },
    "hypertrophy": {
        "method": "Double Progression",
        "increment": "Increase reps to top of range, then add weight and reset to bottom",
        "deload": "Reduce weight by 20% every 5-6 weeks",
    },
    "endurance": {
        "method": "Volume Progression",
        "increment": "Add 1-2 reps per set each week until reaching 25 reps",
        "deload": "Reduce volume by 40% every 4 weeks",
    },
    "weight_loss": {
        "method": "Density Progression",
        "increment": "Reduce rest periods by 5-10 seconds each week",
        "deload": "Return to original rest periods every 4 weeks",
    },
}


class ValidationError(Exception):
    """Raised when input validation fails."""
    pass


def validate_input(data):
    """Validate workout suggester input."""
    required = ["gender", "goal", "experience", "equipment", "days_per_week"]
    for field in required:
        if field not in data:
            raise ValidationError(f"Missing required field: {field}")

    if data["gender"] not in VALID_GENDERS:
        raise ValidationError(f"gender must be one of: {', '.join(VALID_GENDERS)}")

    if data["goal"] not in VALID_GOALS:
        raise ValidationError(f"goal must be one of: {', '.join(VALID_GOALS)}")

    if data["experience"] not in VALID_EXPERIENCE:
        raise ValidationError(f"experience must be one of: {', '.join(VALID_EXPERIENCE)}")

    if not isinstance(data["equipment"], list):
        raise ValidationError("equipment must be a list")

    invalid_equipment = set(data["equipment"]) - VALID_EQUIPMENT
    if invalid_equipment:
        raise ValidationError(
            f"Invalid equipment: {', '.join(invalid_equipment)}. "
            f"Valid options: {', '.join(VALID_EQUIPMENT)}"
        )

    days = data["days_per_week"]
    if not isinstance(days, int) or days < 3 or days > 6:
        raise ValidationError("days_per_week must be an integer between 3 and 6")

    duration = data.get("session_duration", 60)
    if not isinstance(duration, int) or duration < 30 or duration > 120:
        raise ValidationError("session_duration must be an integer between 30 and 120")


def get_muscle_groups_for_day(day_info, gender, split_type):
    """Get muscle groups and sub-regions for a workout day, adjusted for gender."""
    groups = day_info["muscle_groups"].copy()

    # Get base sub-regions for this split
    target_subregions = {}
    base_subregions = SPLIT_SUBREGIONS.get(split_type, {})
    excluded = set(GENDER_EXCLUDED_SUBREGIONS.get(gender, []))

    for muscle_group, subregions in base_subregions.items():
        # Filter out excluded sub-regions for this gender
        filtered = [sr for sr in subregions if sr not in excluded]
        if filtered:
            target_subregions[muscle_group] = filtered.copy()

    # Female: prioritize glutes on leg days
    if gender == "female" and "legs" in groups:
        if "legs" in target_subregions:
            leg_subs = target_subregions["legs"]
            if "glutes" in leg_subs:
                leg_subs.remove("glutes")
                leg_subs.insert(0, "glutes")

    return groups, target_subregions


def build_workout_day(day_info, selector, goal_params, experience, gender,
                      excluded_lower_tier_ids=None):
    """Build a single workout day with intelligent exercise selection.

    Uses the new ExerciseSelector for:
    - Sub-region coverage
    - Tier-based prioritization
    - Movement pattern redundancy prevention
    - Gender-specific volume (females: more legs/glutes)
    - Enforces min 4 and max 9 exercises per workout
    - Variant-based exercise differentiation (excludes lower-tier exercises
      used in other variants while keeping S+/S tier consistent)

    Args:
        day_info: Day configuration from SPLITS
        selector: ExerciseSelector instance
        goal_params: Goal-specific parameters (sets, reps, rest)
        experience: User experience level
        gender: User gender
        excluded_lower_tier_ids: Set of exercise IDs to exclude for variant
                                 differentiation. S+/S tier exercises are
                                 never excluded.
    """
    exercises = []
    all_warnings = []
    volume_mult = EXPERIENCE_MULTIPLIERS[experience]
    gender_adjustments = GENDER_VOLUME_ADJUSTMENTS[gender]

    if excluded_lower_tier_ids is None:
        excluded_lower_tier_ids = set()

    split_type = day_info.get("split_type", "full_body")
    muscle_groups, target_subregions = get_muscle_groups_for_day(
        day_info, gender, split_type
    )

    # Track used patterns across the entire workout day
    used_patterns = set()

    # For full body, reduce volume per muscle to avoid excessive session length
    is_full_body = len(muscle_groups) >= 4

    # Calculate exercises needed per muscle group considering gender adjustments
    exercises_by_muscle = {}

    for muscle_group in muscle_groups:
        # Get target sub-regions for this muscle in this split
        sub_targets = target_subregions.get(muscle_group)

        # Apply gender-specific volume adjustment
        gender_mult = gender_adjustments.get(muscle_group, 1.0)

        # Temporarily adjust selector config for this muscle group
        original_exercises_per_muscle = selector.config["exercises_per_muscle"]
        adjusted_count = max(1, round(original_exercises_per_muscle * gender_mult))
        selector.config["exercises_per_muscle"] = adjusted_count

        # Select exercises with intelligent algorithm
        # Pass excluded_lower_tier_ids for variant differentiation
        selected, used_patterns, warnings = selector.select_for_muscle_group(
            muscle_group,
            used_patterns=used_patterns,
            target_subregions=sub_targets,
            excluded_exercise_ids=excluded_lower_tier_ids,
        )

        # Restore original config
        selector.config["exercises_per_muscle"] = original_exercises_per_muscle

        all_warnings.extend(warnings)

        # For full body, limit exercises per muscle
        if is_full_body and len(selected) > 2:
            selected = selected[:2]

        exercises_by_muscle[muscle_group] = selected

    # Flatten and apply constraints
    all_selected = []
    for muscle_group in muscle_groups:
        all_selected.extend(exercises_by_muscle[muscle_group])

    # Sort: compounds first, then isolations (preserving tier order within each group)
    compounds = [e for e in all_selected if e.get("type") == "compound"]
    isolations = [e for e in all_selected if e.get("type") == "isolation"]
    all_selected = compounds + isolations

    # Enforce gender-specific maximum exercises
    gender_max = GENDER_MAX_EXERCISES[gender].get(split_type, WORKOUT_CONSTRAINTS["max_exercises"])
    max_exercises = min(gender_max, WORKOUT_CONSTRAINTS["max_exercises"])
    if len(all_selected) > max_exercises:
        # Keep compounds, trim isolations first
        compounds = [e for e in all_selected if e.get("type") == "compound"]
        isolations = [e for e in all_selected if e.get("type") == "isolation"]
        remaining_slots = max_exercises - len(compounds)
        if remaining_slots > 0:
            all_selected = compounds + isolations[:remaining_slots]
        else:
            all_selected = compounds[:max_exercises]

    # Enforce minimum 4 exercises - fill with more from the same split's sub-regions
    min_exercises = WORKOUT_CONSTRAINTS["min_exercises"]
    if len(all_selected) < min_exercises:
        selected_ids = {e["id"] for e in all_selected}
        needed = min_exercises - len(all_selected)

        # Get sub-regions for the current split type
        split_subregions = target_subregions if target_subregions else {}
        fill_subregions = []
        for mg in muscle_groups:
            if mg in split_subregions:
                fill_subregions.extend(split_subregions[mg])

        # If legs split, prioritize glutes
        if split_type == "legs":
            if "glutes" in fill_subregions:
                fill_subregions.remove("glutes")
                fill_subregions.insert(0, "glutes")

        # First pass: try to fill respecting exclusions
        for subregion in fill_subregions:
            if needed <= 0:
                break
            candidates = selector._get_exercises_for_subregion(subregion)
            for exercise in candidates:
                if exercise["id"] in selected_ids:
                    continue
                # Skip excluded exercises (for variant differentiation)
                # but S+/S tier exercises are never excluded
                if exercise["id"] in excluded_lower_tier_ids:
                    tier = exercise.get("nippard_tier")
                    if tier not in ("S+", "S"):
                        continue
                ex_pattern = get_movement_pattern(exercise["id"])
                if ex_pattern and ex_pattern in used_patterns:
                    continue
                all_selected.append(exercise)
                selected_ids.add(exercise["id"])
                if ex_pattern:
                    used_patterns.add(ex_pattern)
                needed -= 1
                if needed <= 0:
                    break

        # Second pass: if still not enough, allow excluded exercises
        # (prioritize meeting minimum over variant differentiation)
        if needed > 0:
            for subregion in fill_subregions:
                if needed <= 0:
                    break
                candidates = selector._get_exercises_for_subregion(subregion)
                for exercise in candidates:
                    if exercise["id"] in selected_ids:
                        continue
                    ex_pattern = get_movement_pattern(exercise["id"])
                    if ex_pattern and ex_pattern in used_patterns:
                        continue
                    all_selected.append(exercise)
                    selected_ids.add(exercise["id"])
                    if ex_pattern:
                        used_patterns.add(ex_pattern)
                    needed -= 1
                    if needed <= 0:
                        break

    # Re-sort after adding minimum exercises: compounds first
    compounds = [e for e in all_selected if e.get("type") == "compound"]
    isolations = [e for e in all_selected if e.get("type") == "isolation"]
    all_selected = compounds + isolations

    # Build final exercise list with parameters
    for exercise in all_selected:
        sets = max(2, round(goal_params["sets"] * volume_mult))
        rest = exercise.get("rest", goal_params["rest"])

        if exercise["type"] == "isolation":
            rest = min(rest, 90)

        # Get tier for display
        tier = exercise.get("nippard_tier", "-")

        exercises.append({
            "id": exercise["id"],
            "name": exercise["name"],
            "muscle_group": exercise["muscle_group"],
            "sub_region": exercise["sub_region"],
            "sets": sets,
            "reps": goal_params["reps"],
            "rest_seconds": rest,
            "type": exercise["type"],
            "tier": tier,
            "targets": exercise.get("targets", []),
        })

    return {
        "day": day_info["name"],
        "variant": day_info.get("variant"),
        "split_type": split_type,
        "muscle_groups": muscle_groups,
        "exercises": exercises,
        "warnings": all_warnings,
    }


def suggest(data):
    """Generate a workout plan based on user parameters.

    Returns a complete workout plan with:
    - Exercises selected for proper muscle head coverage
    - No redundant movement patterns
    - Higher-tier exercises prioritized
    - Difficulty appropriate for experience level
    - Variant-based exercise variation (S+/S exercises stay consistent
      across variants, lower-tier exercises differ)
    """
    validate_input(data)

    equipment = data["equipment"]
    if "bodyweight" not in equipment:
        equipment = equipment + ["bodyweight"]

    # Create the intelligent exercise selector
    selector = ExerciseSelector(equipment, data["experience"])

    split = SPLITS[data["days_per_week"]]
    goal_params = GOAL_PARAMS[data["goal"]]
    progression = PROGRESSIONS[data["goal"]]

    workouts = []
    all_plan_warnings = []

    # Track lower-tier exercises used per variant group
    # Structure: {"push": {"A": set(), "B": set()}, ...}
    # This ensures variant B excludes exercises from variant A (except S+/S tier)
    variant_lower_tier_used = {}

    for day_info in split["days"]:
        variant_group = day_info.get("variant_group")
        variant = day_info.get("variant")

        # Determine which exercises to exclude for this variant
        excluded_lower_tier_ids = set()
        if variant_group and variant:
            if variant_group not in variant_lower_tier_used:
                variant_lower_tier_used[variant_group] = {}

            # Exclude lower-tier exercises from previous variants in this group
            for prev_variant, prev_ids in variant_lower_tier_used[variant_group].items():
                if prev_variant != variant:
                    excluded_lower_tier_ids.update(prev_ids)

        workout = build_workout_day(
            day_info, selector, goal_params,
            data["experience"], data["gender"],
            excluded_lower_tier_ids=excluded_lower_tier_ids
        )

        # Track lower-tier exercises used in this workout for future variants
        if variant_group and variant:
            lower_tier_ids = selector.get_lower_tier_exercise_ids(
                [e for e in workout["exercises"]]
            )
            # Note: workout["exercises"] has processed format, need to check tier field
            lower_tier_ids = {
                e["id"] for e in workout["exercises"]
                if e.get("tier") not in ("S+", "S")
            }
            variant_lower_tier_used[variant_group][variant] = lower_tier_ids

        # Validate the workout against targeted sub-regions (split-aware)
        target_subs = SPLIT_SUBREGIONS.get(workout["split_type"], {})
        validation_warnings = validate_workout(
            workout["exercises"],
            workout["muscle_groups"],
            target_subregions=target_subs if target_subs else None
        )
        workout["validation_warnings"] = validation_warnings
        all_plan_warnings.extend(validation_warnings)

        workouts.append(workout)

    return {
        "split": {
            "name": split["name"],
            "days": [
                {"name": d["name"], "muscle_groups": d["muscle_groups"]}
                for d in split["days"]
            ],
        },
        "workouts": workouts,
        "progression": progression,
        "parameters": {
            "goal": data["goal"],
            "experience": data["experience"],
            "days_per_week": data["days_per_week"],
            "session_duration": data.get("session_duration", 60),
        },
        "warnings": all_plan_warnings,
    }
