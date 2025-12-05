# Workout Day Variation

## Overview

Add variation between similar workout days in the same split (e.g., Push A vs Push B, Full Body A vs Full Body B vs Full Body C). S+ and S tier exercises (the "main lifts") remain consistent across both days, while lower-tier exercises vary to provide training diversity and target sub-regions from different angles.

## User Stories

1. As a user following a 6-day PPL split, I want Push A and Push B to have different secondary exercises so my training has variety while still hitting the core lifts consistently.

2. As a user on a 3-day full body program, I want each workout day to include different exercise selections so I'm not doing the exact same routine three times per week.

3. As a user doing Upper/Lower 4x/week, I want Upper A and Upper B to share the main compound lifts but differ in isolation and accessory work.

## Acceptance Criteria

1. **S+ and S tier exercises remain consistent** - All workouts of the same type (e.g., all Push days) include the same S+ and S tier exercises that are selected.

2. **Lower-tier exercises vary between days** - A+ and below exercises differ between A/B variants (or A/B/C for full body).

3. **Sub-region coverage maintained** - Each day variant still covers all required sub-regions for that split type.

4. **Movement pattern constraints respected** - No redundant movement patterns within a single workout day; variation happens across days, not within them.

5. **Day naming reflects variation** - Days are clearly named (Push A, Push B) and the UI displays them as distinct workouts.

6. **Exercise count consistency** - All variants of the same day type have similar exercise counts (within 1 exercise).

## Technical Requirements

### Backend Changes

**workout_suggester.py:**
- Add `day_variant` parameter (e.g., "A", "B", "C") to `build_workout_day()`
- Pass variant info to the exercise selector
- Track which lower-tier exercises have been used in previous variants

**workout_generator.py:**
- Add `excluded_exercise_ids` parameter to `select_for_muscle_group()` to skip exercises already used in another variant
- Modify Phase 2 (filling remaining volume) to use different exercises based on variant
- S+/S selection in Phase 0 remains unchanged (these are always included)

### Data Model Changes

**Workout day structure:**
```python
{
    "day": "Push A",
    "variant": "A",  # New field
    "split_type": "push",
    "exercises": [...],
    # ... rest unchanged
}
```

### Algorithm Logic

1. **Phase 0 (S+/S tier):** Select top-tier exercises as normal - these are shared across all variants
2. **Phase 1 (Sub-region coverage):** For each variant, exclude exercises already selected in previous variants when filling sub-region slots
3. **Phase 2 (Volume filling):** Cycle through remaining exercises based on variant index

**Variant exercise selection strategy:**
- For 2 variants (A/B): Odd-ranked exercises go to A, even-ranked go to B (after excluding S+/S)
- For 3 variants (A/B/C): Modulo 3 distribution

### API Contract

No changes to the API request/response structure. The variation is automatic based on split configuration.

## Dependencies

- `workout_suggester.py` - Main workout generation orchestration
- `workout_generator.py` - Exercise selection algorithm
- `SPLITS` config in `workout_suggester.py` - Already has A/B naming

## Edge Cases and Error States

1. **Insufficient exercises for variation** - If a muscle group has too few available exercises to vary between days, use the same exercises for both variants. Log a warning but don't fail.

2. **Equipment constraints limiting options** - When limited equipment reduces available exercises, variation may be minimal. This is acceptable; prioritize sub-region coverage over variation.

3. **Single-day splits** - 5-day PPL has mixed structure (Push, Pull, Legs, Upper, Lower). Only the repeated day types (none in this case) would have variation applied.

4. **Beginner volume** - Beginners have fewer exercises per muscle; variation pool is smaller. Accept less variation for beginners.

5. **S+ and S overlap prevention** - If two variants would share the same S+ exercise but have different S tier available, still prioritize consistency over variety.
