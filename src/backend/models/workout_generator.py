"""Intelligent workout generation with sub-region coverage and redundancy prevention.

This module provides evidence-based exercise selection that ensures:
1. All muscle heads/sub-regions are appropriately covered
2. No redundant movement patterns in the same workout
3. Higher-tier exercises are prioritized (S+ > S > A+ > A > B+ > B > C > D)
4. Exercise difficulty matches user experience level
"""

from .exercise_data import (
    ALL_EXERCISES,
    SUB_REGIONS,
    TIER_RANK,
    DIFFICULTY_RANK,
)
from .movement_patterns import get_movement_pattern, are_exercises_redundant


# Volume guidelines by experience level
# Format: (min_exercises, max_exercises, require_all_subregions)
VOLUME_BY_EXPERIENCE = {
    "beginner": {
        "exercises_per_muscle": 2,
        "max_difficulty": "medium",  # No hard exercises for beginners
        "require_all_subregions": False,  # Just hit major areas
    },
    "intermediate": {
        "exercises_per_muscle": 3,
        "max_difficulty": "hard",
        "require_all_subregions": True,  # Cover all heads
    },
    "advanced": {
        "exercises_per_muscle": 4,
        "max_difficulty": "hard",
        "require_all_subregions": True,  # Full coverage with variety
    },
}

# Workout-level constraints
WORKOUT_CONSTRAINTS = {
    "min_exercises": 4,  # No workout should have fewer than 4 exercises
    "max_exercises": 9,  # No workout should exceed 9 exercises
}

# Priority sub-regions for beginners (hit these first when not requiring all)
PRIORITY_SUBREGIONS = {
    "chest": ["mid_chest", "upper_chest"],
    "arms": ["biceps_long_head", "triceps_long_head"],  # Biggest heads
    "shoulders": ["side_delt", "front_delt"],  # Side delts for width
    "back": ["lats", "upper_back"],
    "legs": ["quadriceps", "glutes"],
}

# Sub-region groupings for split workouts (which sub-regions belong to which split)
SPLIT_SUBREGIONS = {
    "push": {
        "chest": ["upper_chest", "mid_chest", "lower_chest"],
        "shoulders": ["front_delt", "side_delt"],
        "arms": ["triceps_lateral_medial", "triceps_long_head"],
    },
    "pull": {
        "back": ["upper_back", "lats"],  # Lower back often trained separately
        "shoulders": ["rear_delt"],
        "arms": ["biceps_short_head", "biceps_long_head"],
    },
    "legs": {
        "legs": ["quadriceps", "hamstrings", "glutes"],
        "back": ["lower_back"],  # Optional
    },
}

# Essential movement patterns that MUST be included per muscle group if available
# These are the "main lifts" that define each muscle group's training
ESSENTIAL_PATTERNS = {
    "back": ["back_vertical_pull", "back_horizontal_row_close"],  # Lat pulldown + Row
    "chest": ["chest_horizontal_press", "chest_incline_press"],  # Flat + Incline press
    "legs": ["quad_squat_bilateral", "quad_leg_extension"],  # Squat + Leg extension
    "shoulders": ["shoulder_overhead_press", "shoulder_lateral_raise_cable"],  # Press + Lateral
    "arms": ["triceps_pushdown", "biceps_cable_curl"],  # Pushdown + Curl
}


class ExerciseSelector:
    """Intelligent exercise selection for workout generation."""

    def __init__(self, available_equipment: list[str], experience: str):
        """Initialize selector with constraints.

        Args:
            available_equipment: List of available equipment
            experience: User experience level (beginner, intermediate, advanced)
        """
        self.equipment = set(available_equipment)
        self.experience = experience
        self.config = VOLUME_BY_EXPERIENCE[experience]

        # Filter exercises by equipment availability
        self.available_exercises = [
            e for e in ALL_EXERCISES
            if set(e["equipment"]).issubset(self.equipment)
        ]

        # Further filter by difficulty
        max_diff_rank = DIFFICULTY_RANK[self.config["max_difficulty"]]
        self.available_exercises = [
            e for e in self.available_exercises
            if DIFFICULTY_RANK.get(e["difficulty"], 1) <= max_diff_rank
        ]

    def _sort_by_tier(self, exercises: list[dict]) -> list[dict]:
        """Sort exercises by Nippard tier (highest first), then by name."""
        return sorted(
            exercises,
            key=lambda e: (-TIER_RANK.get(e.get("nippard_tier"), 0), e["name"])
        )

    def _get_exercises_for_subregion(self, sub_region: str) -> list[dict]:
        """Get all available exercises for a sub-region, sorted by tier."""
        exercises = [
            e for e in self.available_exercises
            if e["sub_region"] == sub_region
        ]
        return self._sort_by_tier(exercises)

    def _get_top_tier_exercises(self, subregions: list[str]) -> list[dict]:
        """Get S+ and S tier exercises for given sub-regions, sorted by tier."""
        top_tier = []
        for subregion in subregions:
            exercises = self._get_exercises_for_subregion(subregion)
            for e in exercises:
                tier = e.get("nippard_tier")
                if tier in ("S+", "S"):
                    top_tier.append(e)
        return self._sort_by_tier(top_tier)

    def _select_with_pattern_diversity(
        self,
        candidates: list[dict],
        target_count: int,
        used_patterns: set[str],
        muscle_group: str = None,
    ) -> tuple[list[dict], set[str]]:
        """Select exercises ensuring movement pattern diversity.

        Prioritizes essential patterns first, then fills with other top-tier exercises.
        """
        selected = []
        selected_ids = set()

        # Group candidates by movement pattern
        by_pattern = {}
        for e in candidates:
            pattern = get_movement_pattern(e["id"])
            if pattern:
                if pattern not in by_pattern:
                    by_pattern[pattern] = []
                by_pattern[pattern].append(e)

        # Phase 1: MUST include essential patterns first (main lifts)
        essential = ESSENTIAL_PATTERNS.get(muscle_group, [])
        for pattern in essential:
            if len(selected) >= target_count:
                break
            if pattern in used_patterns:
                continue
            if pattern not in by_pattern:
                continue

            # Get the best exercise for this essential pattern
            for e in by_pattern[pattern]:
                if e["id"] not in selected_ids:
                    selected.append(e)
                    selected_ids.add(e["id"])
                    used_patterns.add(pattern)
                    break

        # Phase 2: Fill with other top-tier exercises (one per pattern for diversity)
        for pattern, exercises in sorted(by_pattern.items(), key=lambda x: -TIER_RANK.get(x[1][0].get("nippard_tier"), 0)):
            if len(selected) >= target_count:
                break
            if pattern in used_patterns:
                continue

            for e in exercises:
                if e["id"] not in selected_ids:
                    selected.append(e)
                    selected_ids.add(e["id"])
                    used_patterns.add(pattern)
                    break

        # Phase 3: Fill remaining slots with best remaining exercises (by tier)
        remaining = [e for e in candidates if e["id"] not in selected_ids]
        remaining = self._sort_by_tier(remaining)

        for e in remaining:
            if len(selected) >= target_count:
                break
            pattern = get_movement_pattern(e["id"])
            if pattern and pattern in used_patterns:
                continue
            selected.append(e)
            selected_ids.add(e["id"])
            if pattern:
                used_patterns.add(pattern)

        return selected, used_patterns

    def select_for_muscle_group(
        self,
        muscle_group: str,
        used_patterns: set[str] | None = None,
        target_subregions: list[str] | None = None,
    ) -> tuple[list[dict], set[str], list[str]]:
        """Select exercises for a muscle group with intelligent coverage.

        Args:
            muscle_group: The muscle group (chest, arms, shoulders, back, legs)
            used_patterns: Movement patterns already used (for redundancy check)
            target_subregions: Specific sub-regions to target (for split workouts)

        Returns:
            Tuple of (selected_exercises, updated_used_patterns, warnings)
        """
        if used_patterns is None:
            used_patterns = set()

        warnings = []
        selected = []
        selected_ids = set()

        # Determine which sub-regions to target
        if target_subregions:
            subregions = target_subregions
        else:
            subregions = SUB_REGIONS.get(muscle_group, [])

        # For beginners, prioritize main sub-regions
        if not self.config["require_all_subregions"]:
            priority = PRIORITY_SUBREGIONS.get(muscle_group, subregions[:2])
            subregions = [sr for sr in priority if sr in subregions]

        target_count = self.config["exercises_per_muscle"]
        covered_subregions = set()

        # Phase 0: ALWAYS include top-tier (S+, S) exercises first - these are the "main" lifts
        # Use pattern diversity to ensure variety (e.g., both vertical pull AND horizontal row for back)
        top_tier_exercises = self._get_top_tier_exercises(subregions)
        phase0_selected, used_patterns = self._select_with_pattern_diversity(
            top_tier_exercises, target_count, used_patterns, muscle_group
        )

        for exercise in phase0_selected:
            selected.append(exercise)
            selected_ids.add(exercise["id"])
            covered_subregions.add(exercise["sub_region"])

        # Phase 1: Ensure each target sub-region has at least one exercise
        for subregion in subregions:
            if len(selected) >= target_count:
                break

            if subregion in covered_subregions:
                continue  # Already covered by top-tier exercise

            candidates = self._get_exercises_for_subregion(subregion)

            for exercise in candidates:
                if exercise["id"] in selected_ids:
                    continue

                pattern = get_movement_pattern(exercise["id"])
                if pattern and pattern in used_patterns:
                    continue

                # Found a valid exercise
                selected.append(exercise)
                selected_ids.add(exercise["id"])
                covered_subregions.add(subregion)
                if pattern:
                    used_patterns.add(pattern)
                break
            else:
                # No valid exercise found for this sub-region
                if self.config["require_all_subregions"]:
                    warnings.append(
                        f"Could not find non-redundant exercise for {subregion}"
                    )

        # Phase 2: Fill remaining volume with best available exercises
        while len(selected) < target_count:
            best_candidate = None
            best_tier = -1

            # Look through all sub-regions for the best remaining exercise
            for subregion in subregions:
                candidates = self._get_exercises_for_subregion(subregion)

                for exercise in candidates:
                    if exercise["id"] in selected_ids:
                        continue

                    pattern = get_movement_pattern(exercise["id"])
                    if pattern and pattern in used_patterns:
                        continue

                    tier = TIER_RANK.get(exercise.get("nippard_tier"), 0)

                    # Prefer exercises from uncovered sub-regions
                    if subregion not in covered_subregions:
                        tier += 10  # Big bonus for new coverage

                    if tier > best_tier:
                        best_tier = tier
                        best_candidate = exercise

            if best_candidate is None:
                # No more valid exercises available
                break

            selected.append(best_candidate)
            selected_ids.add(best_candidate["id"])
            covered_subregions.add(best_candidate["sub_region"])
            pattern = get_movement_pattern(best_candidate["id"])
            if pattern:
                used_patterns.add(pattern)

        # Check coverage and generate warnings
        missing = set(subregions) - covered_subregions
        if missing and self.config["require_all_subregions"]:
            warnings.append(f"Missing coverage for: {', '.join(missing)}")

        return selected, used_patterns, warnings

    def select_for_split(
        self,
        split_type: str,
        muscle_groups: list[str],
    ) -> tuple[list[dict], list[str]]:
        """Select exercises for a workout split (push/pull/legs/upper/lower).

        Args:
            split_type: Type of split for sub-region targeting
            muscle_groups: Muscle groups to include

        Returns:
            Tuple of (selected_exercises, warnings)
        """
        all_selected = []
        all_warnings = []
        used_patterns = set()

        # Get sub-region mappings for this split type
        split_map = SPLIT_SUBREGIONS.get(split_type, {})

        for muscle_group in muscle_groups:
            # Determine target sub-regions
            if muscle_group in split_map:
                target_subregions = split_map[muscle_group]
            else:
                target_subregions = None

            selected, used_patterns, warnings = self.select_for_muscle_group(
                muscle_group,
                used_patterns=used_patterns,
                target_subregions=target_subregions,
            )

            all_selected.extend(selected)
            all_warnings.extend(warnings)

        return all_selected, all_warnings


def generate_workout(
    split_type: str,
    muscle_groups: list[str],
    equipment: list[str],
    experience: str,
) -> dict:
    """Generate a complete workout with intelligent exercise selection.

    Args:
        split_type: Type of workout (push, pull, legs, upper, lower, full_body)
        muscle_groups: List of muscle groups to train
        equipment: Available equipment
        experience: User experience level

    Returns:
        Dict with exercises, warnings, and metadata
    """
    selector = ExerciseSelector(equipment, experience)
    exercises, warnings = selector.select_for_split(split_type, muscle_groups)

    return {
        "split_type": split_type,
        "exercises": exercises,
        "warnings": warnings,
        "muscle_groups": muscle_groups,
        "experience": experience,
    }


def validate_workout(
    exercises: list[dict],
    muscle_groups: list[str],
    target_subregions: dict[str, list[str]] | None = None
) -> list[str]:
    """Validate a workout for proper coverage and redundancy.

    Args:
        exercises: List of exercise dicts
        muscle_groups: Expected muscle groups
        target_subregions: Optional dict mapping muscle_group -> list of expected sub-regions.
                          If provided, only checks for these specific sub-regions.
                          If None, checks all sub-regions for each muscle group.

    Returns:
        List of warning messages
    """
    warnings = []

    # Group exercises by muscle group
    by_muscle = {}
    for e in exercises:
        mg = e["muscle_group"]
        if mg not in by_muscle:
            by_muscle[mg] = []
        by_muscle[mg].append(e)

    # Check sub-region coverage for each muscle group
    for muscle_group in muscle_groups:
        if muscle_group not in by_muscle:
            warnings.append(f"No exercises for {muscle_group}")
            continue

        muscle_exercises = by_muscle[muscle_group]
        covered = {e["sub_region"] for e in muscle_exercises}

        # Determine required sub-regions
        if target_subregions and muscle_group in target_subregions:
            required = set(target_subregions[muscle_group])
        else:
            required = set(SUB_REGIONS.get(muscle_group, []))

        missing = required - covered

        if missing:
            warnings.append(
                f"{muscle_group}: missing sub-regions {', '.join(missing)}"
            )

    # Check for movement pattern redundancy
    patterns_seen = {}
    for e in exercises:
        pattern = get_movement_pattern(e["id"])
        if pattern:
            if pattern in patterns_seen:
                warnings.append(
                    f"Redundant pattern '{pattern}': "
                    f"{patterns_seen[pattern]} and {e['name']}"
                )
            else:
                patterns_seen[pattern] = e["name"]

    return warnings
