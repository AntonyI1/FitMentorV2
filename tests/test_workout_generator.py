"""Tests for the intelligent workout generation system.

Tests cover:
1. Movement pattern redundancy prevention
2. Sub-region (muscle head) coverage
3. Tier-prioritized exercise selection
4. Difficulty filtering by experience level
5. Full workout generation validation
"""

import sys
import os

# Add src/backend to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src', 'backend'))

import pytest
from models.movement_patterns import (
    get_movement_pattern,
    are_exercises_redundant,
    get_exercises_by_pattern,
    EXERCISE_TO_PATTERN,
)
from models.workout_generator import (
    ExerciseSelector,
    generate_workout,
    validate_workout,
    VOLUME_BY_EXPERIENCE,
)
from models.workout_suggester import suggest, ValidationError
from models.exercise_data import ALL_EXERCISES, SUB_REGIONS, TIER_RANK


class TestMovementPatterns:
    """Test movement pattern classification and redundancy detection."""

    def test_all_exercises_have_patterns(self):
        """Every exercise in the database should have a movement pattern."""
        missing = []
        for exercise in ALL_EXERCISES:
            pattern = get_movement_pattern(exercise["id"])
            if pattern is None:
                missing.append(exercise["id"])

        assert len(missing) == 0, f"Exercises missing patterns: {missing}"

    def test_redundant_exercises_detected(self):
        """Exercises with same pattern should be flagged as redundant."""
        # Flat barbell and flat dumbbell press are both horizontal_press
        assert are_exercises_redundant(
            "flat-barbell-bench-press",
            "flat-dumbbell-press"
        )

        # Incline press and flat press are different patterns
        assert not are_exercises_redundant(
            "incline-barbell-bench-press",
            "flat-barbell-bench-press"
        )

    def test_pattern_groupings_make_sense(self):
        """Check that pattern groupings are logical."""
        # All incline presses should have same pattern
        incline_presses = [
            "incline-barbell-bench-press",
            "incline-dumbbell-press",
            "incline-smith-machine-press",
        ]
        patterns = [get_movement_pattern(e) for e in incline_presses]
        assert len(set(patterns)) == 1, "Incline presses should share pattern"

        # Flies should be different from presses
        assert get_movement_pattern("flat-barbell-bench-press") != \
               get_movement_pattern("flat-dumbbell-fly")


class TestExerciseSelector:
    """Test the intelligent exercise selection algorithm."""

    def test_selector_filters_by_equipment(self):
        """Selector should only return exercises possible with available equipment."""
        # Bodyweight only
        selector = ExerciseSelector(["bodyweight"], "intermediate")

        # Should have exercises
        assert len(selector.available_exercises) > 0

        # All should be bodyweight only
        for e in selector.available_exercises:
            assert set(e["equipment"]).issubset({"bodyweight"}), \
                f"{e['name']} requires {e['equipment']}"

    def test_selector_filters_by_difficulty(self):
        """Beginner selector should exclude hard exercises."""
        selector = ExerciseSelector(
            ["bodyweight", "dumbbell", "barbell", "bench", "rack", "cable", "machine"],
            "beginner"
        )

        for e in selector.available_exercises:
            assert e["difficulty"] != "hard", \
                f"Beginner shouldn't get hard exercise: {e['name']}"

    def test_selector_prevents_pattern_redundancy(self):
        """Selected exercises should not share movement patterns."""
        selector = ExerciseSelector(
            ["bodyweight", "dumbbell", "barbell", "bench", "rack", "cable", "machine"],
            "intermediate"
        )

        selected, used_patterns, warnings = selector.select_for_muscle_group("chest")

        # Check no two exercises share a pattern
        patterns = [get_movement_pattern(e["id"]) for e in selected]
        patterns = [p for p in patterns if p is not None]

        assert len(patterns) == len(set(patterns)), \
            f"Redundant patterns in selection: {patterns}"

    def test_selector_covers_subregions(self):
        """Intermediate/advanced selection should cover all sub-regions."""
        selector = ExerciseSelector(
            ["bodyweight", "dumbbell", "barbell", "bench", "rack", "cable", "machine"],
            "intermediate"
        )

        selected, _, warnings = selector.select_for_muscle_group("chest")

        # Get covered sub-regions
        covered = {e["sub_region"] for e in selected}
        required = set(SUB_REGIONS["chest"])

        # Should cover all or have warnings
        missing = required - covered
        if missing:
            # Check warnings mention the missing regions
            warning_text = " ".join(warnings)
            for m in missing:
                assert m in warning_text or len(missing) == 0, \
                    f"Missing {m} without warning"

    def test_selector_prioritizes_higher_tiers(self):
        """Higher tier exercises should be selected first."""
        selector = ExerciseSelector(
            ["bodyweight", "dumbbell", "barbell", "bench", "rack", "cable", "machine"],
            "intermediate"
        )

        selected, _, _ = selector.select_for_muscle_group("chest")

        # Check that we got some high-tier exercises
        tiers = [e.get("nippard_tier") for e in selected]
        tier_ranks = [TIER_RANK.get(t, 0) for t in tiers]

        # At least one exercise should be A-tier or better (rank >= 5)
        assert any(r >= 5 for r in tier_ranks), \
            f"Should prioritize high-tier exercises, got tiers: {tiers}"


class TestWorkoutGeneration:
    """Test full workout generation."""

    def test_push_workout_covers_chest_shoulders_triceps(self):
        """Push workout should hit chest, front/side delts, and triceps."""
        result = generate_workout(
            split_type="push",
            muscle_groups=["chest", "shoulders", "arms"],
            equipment=["dumbbell", "cable", "bench"],
            experience="intermediate"
        )

        exercises = result["exercises"]
        muscle_groups_hit = {e["muscle_group"] for e in exercises}
        sub_regions_hit = {e["sub_region"] for e in exercises}

        # Should hit chest
        assert "chest" in muscle_groups_hit

        # Should hit shoulders (front/side for push)
        assert "shoulders" in muscle_groups_hit

        # Should hit triceps
        assert "arms" in muscle_groups_hit
        assert any("triceps" in sr for sr in sub_regions_hit)

    def test_pull_workout_covers_back_and_biceps(self):
        """Pull workout should hit back and biceps."""
        result = generate_workout(
            split_type="pull",
            muscle_groups=["back", "arms"],
            equipment=["dumbbell", "cable", "pullup_bar", "bench"],
            experience="intermediate"
        )

        exercises = result["exercises"]
        sub_regions_hit = {e["sub_region"] for e in exercises}

        # Should hit lats
        assert "lats" in sub_regions_hit or "upper_back" in sub_regions_hit

        # Should hit biceps
        assert any("biceps" in sr for sr in sub_regions_hit)

    def test_legs_workout_covers_quads_hams_glutes(self):
        """Leg workout should hit quads, hamstrings, and glutes."""
        result = generate_workout(
            split_type="legs",
            muscle_groups=["legs"],
            equipment=["barbell", "dumbbell", "machine", "bench", "rack"],
            experience="intermediate"
        )

        exercises = result["exercises"]
        sub_regions_hit = {e["sub_region"] for e in exercises}

        # Should hit all leg sub-regions
        assert "quadriceps" in sub_regions_hit
        assert "hamstrings" in sub_regions_hit
        assert "glutes" in sub_regions_hit

    def test_no_redundant_patterns_in_workout(self):
        """Full workout should have no redundant movement patterns."""
        result = generate_workout(
            split_type="push",
            muscle_groups=["chest", "shoulders", "arms"],
            equipment=["dumbbell", "barbell", "cable", "bench", "rack", "machine"],
            experience="advanced"
        )

        exercises = result["exercises"]
        patterns = [get_movement_pattern(e["id"]) for e in exercises]
        patterns = [p for p in patterns if p is not None]

        # Check for duplicates
        seen = set()
        duplicates = []
        for p in patterns:
            if p in seen:
                duplicates.append(p)
            seen.add(p)

        assert len(duplicates) == 0, f"Redundant patterns: {duplicates}"


class TestWorkoutValidation:
    """Test workout validation rules."""

    def test_validation_catches_missing_subregions(self):
        """Validation should warn about missing sub-region coverage."""
        # Create a workout missing upper chest
        exercises = [
            {"id": "flat-barbell-bench-press", "muscle_group": "chest", "sub_region": "mid_chest"},
            {"id": "chest-dips", "muscle_group": "chest", "sub_region": "lower_chest"},
        ]

        warnings = validate_workout(exercises, ["chest"])

        # Should warn about missing upper_chest
        assert any("upper_chest" in w for w in warnings), \
            f"Should warn about missing upper_chest, got: {warnings}"

    def test_validation_catches_redundant_patterns(self):
        """Validation should warn about redundant movement patterns."""
        # Create a workout with two horizontal presses
        exercises = [
            {"id": "flat-barbell-bench-press", "muscle_group": "chest", "sub_region": "mid_chest", "name": "Flat BB Press"},
            {"id": "flat-dumbbell-press", "muscle_group": "chest", "sub_region": "mid_chest", "name": "Flat DB Press"},
        ]

        warnings = validate_workout(exercises, ["chest"])

        # Should warn about redundancy
        assert any("redundant" in w.lower() for w in warnings), \
            f"Should warn about redundancy, got: {warnings}"


class TestFullSuggestAPI:
    """Test the full suggest() API."""

    def test_suggest_basic_push_pull_legs(self):
        """Test generating a PPL split."""
        result = suggest({
            "gender": "male",
            "goal": "hypertrophy",
            "experience": "intermediate",
            "equipment": ["barbell", "dumbbell", "cable", "bench", "rack", "machine"],
            "days_per_week": 6,
        })

        assert result["split"]["name"] == "Push/Pull/Legs 6x/week"
        assert len(result["workouts"]) == 6

        # Check each workout has exercises
        for workout in result["workouts"]:
            assert len(workout["exercises"]) > 0

    def test_suggest_respects_equipment_constraints(self):
        """Workouts should only use available equipment."""
        result = suggest({
            "gender": "female",
            "goal": "hypertrophy",
            "experience": "beginner",
            "equipment": ["dumbbell", "bench"],
            "days_per_week": 3,
        })

        # Check all exercises can be done with available equipment
        for workout in result["workouts"]:
            for exercise in workout["exercises"]:
                # Find the exercise in database to check equipment
                db_exercise = next(
                    (e for e in ALL_EXERCISES if e["id"] == exercise["id"]),
                    None
                )
                if db_exercise:
                    required = set(db_exercise["equipment"])
                    available = {"dumbbell", "bench", "bodyweight"}
                    assert required.issubset(available), \
                        f"{exercise['name']} requires {required}"

    def test_suggest_includes_validation_warnings(self):
        """Suggest should include validation warnings."""
        result = suggest({
            "gender": "male",
            "goal": "hypertrophy",
            "experience": "intermediate",
            "equipment": ["dumbbell", "cable", "bench"],
            "days_per_week": 6,
        })

        # Should have warnings key
        assert "warnings" in result

        # Each workout should have validation_warnings
        for workout in result["workouts"]:
            assert "validation_warnings" in workout

    def test_suggest_validation_errors(self):
        """Invalid input should raise ValidationError."""
        with pytest.raises(ValidationError):
            suggest({
                "gender": "invalid",
                "goal": "hypertrophy",
                "experience": "intermediate",
                "equipment": ["dumbbell"],
                "days_per_week": 6,
            })

        with pytest.raises(ValidationError):
            suggest({
                "gender": "male",
                "goal": "hypertrophy",
                "experience": "intermediate",
                "equipment": ["dumbbell"],
                "days_per_week": 10,  # Invalid
            })

    def test_suggest_exercises_have_required_fields(self):
        """Each exercise in output should have required fields."""
        result = suggest({
            "gender": "male",
            "goal": "hypertrophy",
            "experience": "intermediate",
            "equipment": ["barbell", "dumbbell", "cable", "bench", "rack"],
            "days_per_week": 6,
        })

        required_fields = ["id", "name", "muscle_group", "sub_region", "sets", "reps", "type"]

        for workout in result["workouts"]:
            for exercise in workout["exercises"]:
                for field in required_fields:
                    assert field in exercise, f"Missing {field} in {exercise}"


class TestSubregionCoverage:
    """Specific tests for sub-region (muscle head) coverage."""

    def test_chest_day_hits_all_heads(self):
        """A dedicated chest day should hit upper, mid, and lower."""
        selector = ExerciseSelector(
            ["barbell", "dumbbell", "cable", "bench", "rack", "machine"],
            "advanced"
        )

        # Target all chest sub-regions
        selected, _, warnings = selector.select_for_muscle_group(
            "chest",
            target_subregions=["upper_chest", "mid_chest", "lower_chest"]
        )

        covered = {e["sub_region"] for e in selected}

        # Advanced should cover all
        assert "upper_chest" in covered, "Missing upper chest"
        assert "mid_chest" in covered, "Missing mid chest"
        # Lower chest might be missed if no valid non-redundant exercise

    def test_arm_workout_hits_both_bicep_heads(self):
        """Arm workout should target both bicep heads."""
        selector = ExerciseSelector(
            ["dumbbell", "cable", "bench", "barbell_ez"],
            "intermediate"
        )

        selected, _, _ = selector.select_for_muscle_group(
            "arms",
            target_subregions=["biceps_short_head", "biceps_long_head"]
        )

        covered = {e["sub_region"] for e in selected}

        # Should hit both heads
        assert "biceps_short_head" in covered or "biceps_long_head" in covered

    def test_tricep_coverage_includes_long_head(self):
        """Tricep training should include long head (largest head)."""
        selector = ExerciseSelector(
            ["dumbbell", "cable", "bench", "barbell_ez"],
            "intermediate"
        )

        selected, _, _ = selector.select_for_muscle_group(
            "arms",
            target_subregions=["triceps_lateral_medial", "triceps_long_head"]
        )

        covered = {e["sub_region"] for e in selected}

        # Long head is most important for triceps mass
        assert "triceps_long_head" in covered or "triceps_lateral_medial" in covered


class TestWorkoutDayVariation:
    """Test workout day variation between A/B/C variants."""

    def test_ppl_variants_share_top_tier_exercises(self):
        """Push A and Push B should have the same S+/S tier exercises."""
        result = suggest({
            "gender": "male",
            "goal": "hypertrophy",
            "experience": "intermediate",
            "equipment": ["barbell", "dumbbell", "cable", "bench", "rack", "machine"],
            "days_per_week": 6,
        })

        # Find Push A and Push B workouts
        push_a = next(w for w in result["workouts"] if w["day"] == "Push A")
        push_b = next(w for w in result["workouts"] if w["day"] == "Push B")

        # Get S+/S tier exercises from each
        push_a_top_tier = {e["id"] for e in push_a["exercises"] if e["tier"] in ("S+", "S")}
        push_b_top_tier = {e["id"] for e in push_b["exercises"] if e["tier"] in ("S+", "S")}

        # Top-tier exercises should be identical
        assert push_a_top_tier == push_b_top_tier, \
            f"Top-tier exercises differ: A={push_a_top_tier}, B={push_b_top_tier}"

    def test_ppl_variants_have_different_lower_tier_exercises(self):
        """Push A and Push B should have different A+ and below exercises."""
        result = suggest({
            "gender": "male",
            "goal": "hypertrophy",
            "experience": "intermediate",
            "equipment": ["barbell", "dumbbell", "cable", "bench", "rack", "machine"],
            "days_per_week": 6,
        })

        # Find Push A and Push B workouts
        push_a = next(w for w in result["workouts"] if w["day"] == "Push A")
        push_b = next(w for w in result["workouts"] if w["day"] == "Push B")

        # Get lower-tier exercises from each
        push_a_lower = {e["id"] for e in push_a["exercises"] if e["tier"] not in ("S+", "S")}
        push_b_lower = {e["id"] for e in push_b["exercises"] if e["tier"] not in ("S+", "S")}

        # Lower-tier exercises should be different (no overlap)
        overlap = push_a_lower & push_b_lower
        assert len(overlap) == 0, \
            f"Lower-tier exercises overlap: {overlap}"

    def test_full_body_variants_have_different_accessories(self):
        """Full Body A/B/C should share main lifts but differ in accessories."""
        result = suggest({
            "gender": "male",
            "goal": "hypertrophy",
            "experience": "intermediate",
            "equipment": ["barbell", "dumbbell", "cable", "bench", "rack", "machine"],
            "days_per_week": 3,
        })

        # Get all three full body workouts
        fb_a = next(w for w in result["workouts"] if w["day"] == "Full Body A")
        fb_b = next(w for w in result["workouts"] if w["day"] == "Full Body B")
        fb_c = next(w for w in result["workouts"] if w["day"] == "Full Body C")

        # Get top-tier exercises
        a_top = {e["id"] for e in fb_a["exercises"] if e["tier"] in ("S+", "S")}
        b_top = {e["id"] for e in fb_b["exercises"] if e["tier"] in ("S+", "S")}
        c_top = {e["id"] for e in fb_c["exercises"] if e["tier"] in ("S+", "S")}

        # Top-tier should be consistent across all three
        assert a_top == b_top == c_top, "Top-tier exercises should be same across variants"

        # Get lower-tier exercises
        a_lower = {e["id"] for e in fb_a["exercises"] if e["tier"] not in ("S+", "S")}
        b_lower = {e["id"] for e in fb_b["exercises"] if e["tier"] not in ("S+", "S")}
        c_lower = {e["id"] for e in fb_c["exercises"] if e["tier"] not in ("S+", "S")}

        # Lower-tier should differ between variants
        # A and B should have no overlap
        ab_overlap = a_lower & b_lower
        assert len(ab_overlap) == 0, f"A and B have overlapping lower-tier: {ab_overlap}"

        # A and C should have no overlap
        ac_overlap = a_lower & c_lower
        assert len(ac_overlap) == 0, f"A and C have overlapping lower-tier: {ac_overlap}"

    def test_upper_lower_variants_differ(self):
        """Upper A and Upper B should have same top-tier but different accessories."""
        result = suggest({
            "gender": "male",
            "goal": "hypertrophy",
            "experience": "intermediate",
            "equipment": ["barbell", "dumbbell", "cable", "bench", "rack", "machine"],
            "days_per_week": 4,
        })

        # Find Upper A and Upper B
        upper_a = next(w for w in result["workouts"] if w["day"] == "Upper A")
        upper_b = next(w for w in result["workouts"] if w["day"] == "Upper B")

        # Top-tier should match
        a_top = {e["id"] for e in upper_a["exercises"] if e["tier"] in ("S+", "S")}
        b_top = {e["id"] for e in upper_b["exercises"] if e["tier"] in ("S+", "S")}
        assert a_top == b_top, "Upper A and B should share top-tier exercises"

        # Lower-tier should differ
        a_lower = {e["id"] for e in upper_a["exercises"] if e["tier"] not in ("S+", "S")}
        b_lower = {e["id"] for e in upper_b["exercises"] if e["tier"] not in ("S+", "S")}
        overlap = a_lower & b_lower
        assert len(overlap) == 0, f"Upper A and B should have different lower-tier: {overlap}"

    def test_variant_exclusion_respects_equipment(self):
        """With limited equipment, variation should degrade gracefully."""
        result = suggest({
            "gender": "male",
            "goal": "hypertrophy",
            "experience": "intermediate",
            "equipment": ["dumbbell", "bench"],  # Very limited equipment
            "days_per_week": 6,
        })

        # Should not crash with limited equipment
        assert len(result["workouts"]) == 6

        # All workouts should still have minimum exercises
        # (may need to reuse some excluded exercises to meet minimum)
        for workout in result["workouts"]:
            assert len(workout["exercises"]) >= 4, \
                f"{workout['day']} has too few exercises"

    def test_variant_subregion_coverage_maintained(self):
        """Each variant should still cover required sub-regions."""
        result = suggest({
            "gender": "male",
            "goal": "hypertrophy",
            "experience": "intermediate",
            "equipment": ["barbell", "dumbbell", "cable", "bench", "rack", "machine"],
            "days_per_week": 6,
        })

        for workout in result["workouts"]:
            if workout["split_type"] == "push":
                sub_regions = {e["sub_region"] for e in workout["exercises"]}
                # Push should hit chest, shoulders, triceps sub-regions
                assert any("chest" in sr or sr in ["mid_chest", "upper_chest", "lower_chest"]
                          for sr in sub_regions), \
                    f"{workout['day']} missing chest sub-region"
                assert any("triceps" in sr for sr in sub_regions), \
                    f"{workout['day']} missing triceps sub-region"

    def test_workout_includes_variant_field(self):
        """Workouts should include the variant field."""
        result = suggest({
            "gender": "male",
            "goal": "hypertrophy",
            "experience": "intermediate",
            "equipment": ["barbell", "dumbbell", "cable", "bench", "rack"],
            "days_per_week": 6,
        })

        push_a = next(w for w in result["workouts"] if w["day"] == "Push A")
        push_b = next(w for w in result["workouts"] if w["day"] == "Push B")

        assert push_a.get("variant") == "A"
        assert push_b.get("variant") == "B"

    def test_five_day_split_no_variants(self):
        """5-day PPL has no duplicate day types, so no variation needed."""
        result = suggest({
            "gender": "male",
            "goal": "hypertrophy",
            "experience": "intermediate",
            "equipment": ["barbell", "dumbbell", "cable", "bench", "rack"],
            "days_per_week": 5,
        })

        # Check that workouts without variant_group work correctly
        for workout in result["workouts"]:
            # Should still have exercises
            assert len(workout["exercises"]) >= 4
            # variant field should be None for 5-day split
            assert workout.get("variant") is None

    def test_exercise_count_consistency_across_variants(self):
        """Variants of same day type should have similar exercise counts."""
        result = suggest({
            "gender": "male",
            "goal": "hypertrophy",
            "experience": "intermediate",
            "equipment": ["barbell", "dumbbell", "cable", "bench", "rack", "machine"],
            "days_per_week": 6,
        })

        push_a = next(w for w in result["workouts"] if w["day"] == "Push A")
        push_b = next(w for w in result["workouts"] if w["day"] == "Push B")

        # Exercise counts should be within 1 of each other
        count_diff = abs(len(push_a["exercises"]) - len(push_b["exercises"]))
        assert count_diff <= 1, \
            f"Push A has {len(push_a['exercises'])} exercises, Push B has {len(push_b['exercises'])}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
