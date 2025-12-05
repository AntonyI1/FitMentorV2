# Workout Day Variation - Implementation Plan

## Summary

Implement exercise variation between repeated workout days (A/B variants) while keeping S+ and S tier exercises consistent. Lower-tier exercises will differ between variants.

**Complexity:** Medium

## Phases

### Phase 1: Add Variant Tracking to Split Configuration

**Goal:** Identify which days are variants of each other and track variant index.

**Files to modify:**
- `src/backend/models/workout_suggester.py`

**Changes:**
1. Add `variant` and `variant_group` fields to each day in `SPLITS`:
   ```python
   {
       "name": "Push A",
       "split_type": "push",
       "variant": "A",           # New: A, B, or C
       "variant_group": "push",  # New: groups related days
       "muscle_groups": [...]
   }
   ```

2. Update all split configurations:
   - 3-day Full Body: A/B/C variants in "full_body" group
   - 4-day Upper/Lower: A/B variants for "upper" and "lower" groups
   - 5-day PPL+: No duplicates, no variant needed
   - 6-day PPL: A/B variants for "push", "pull", "legs" groups

### Phase 2: Modify ExerciseSelector for Variant-Aware Selection

**Goal:** Allow excluding exercises used in other variants while preserving S+/S tier.

**Files to modify:**
- `src/backend/models/workout_generator.py`

**Changes:**
1. Add `excluded_exercise_ids` parameter to `select_for_muscle_group()`:
   ```python
   def select_for_muscle_group(
       self,
       muscle_group: str,
       used_patterns: set[str] | None = None,
       target_subregions: list[str] | None = None,
       excluded_exercise_ids: set[str] | None = None,  # New
   ) -> tuple[list[dict], set[str], list[str]]:
   ```

2. Modify Phase 0 (S+/S selection): No change - these are always included regardless of exclusions

3. Modify Phase 1 (sub-region coverage): Skip exercises in `excluded_exercise_ids` when filling sub-region slots

4. Modify Phase 2 (volume filling): Skip exercises in `excluded_exercise_ids`

5. Add helper method to extract non-top-tier exercise IDs:
   ```python
   def get_lower_tier_exercise_ids(self, exercises: list[dict]) -> set[str]:
       """Return IDs of exercises that are NOT S+ or S tier."""
       return {e["id"] for e in exercises if e.get("nippard_tier") not in ("S+", "S")}
   ```

### Phase 3: Update Workout Building for Variant Support

**Goal:** Generate different exercise selections for each variant.

**Files to modify:**
- `src/backend/models/workout_suggester.py`

**Changes:**
1. Add `variant_exercises_cache` to track exercises used per variant group:
   ```python
   # In suggest():
   variant_lower_tier_used = {}  # {"push": {"A": set(), "B": set()}}
   ```

2. Modify `build_workout_day()` signature:
   ```python
   def build_workout_day(
       day_info,
       selector,
       goal_params,
       experience,
       gender,
       excluded_lower_tier_ids=None  # New: IDs to exclude
   ):
   ```

3. Update `suggest()` to:
   - Group days by `variant_group`
   - For first variant (A): Generate normally, store lower-tier exercise IDs
   - For subsequent variants (B, C): Pass previous variant's lower-tier IDs as exclusions

4. Add `variant` field to workout output:
   ```python
   return {
       "day": day_info["name"],
       "variant": day_info.get("variant"),  # New
       "split_type": split_type,
       ...
   }
   ```

### Phase 4: Add Tests for Variation Behavior

**Goal:** Verify variants have different lower-tier exercises while sharing top-tier.

**Files to modify:**
- `tests/test_workout_generator.py`

**New test cases:**

1. `test_ppl_variants_share_top_tier_exercises`:
   - Generate 6-day PPL
   - Compare Push A and Push B
   - Assert S+/S exercises are identical
   - Assert A+ and below differ

2. `test_full_body_variants_have_different_accessories`:
   - Generate 3-day Full Body
   - Compare A, B, C variants
   - Assert main lifts shared, secondary exercises differ

3. `test_variant_exclusion_respects_equipment`:
   - With limited equipment
   - Assert variation is reduced gracefully (no crashes)

4. `test_variant_subregion_coverage_maintained`:
   - Each variant still covers required sub-regions
   - No gaps introduced by exclusions

5. `test_upper_lower_variants_differ`:
   - Generate 4-day Upper/Lower
   - Verify Upper A != Upper B (except top-tier)

## Data Models

### Split Day Schema (updated)

```python
{
    "name": str,           # Display name: "Push A"
    "split_type": str,     # workout type: "push"
    "variant": str,        # "A", "B", or "C" (optional)
    "variant_group": str,  # grouping key: "push" (optional)
    "muscle_groups": list  # ["chest", "shoulders", "arms"]
}
```

### Workout Output Schema (updated)

```python
{
    "day": str,                    # "Push A"
    "variant": str | None,         # "A" (new field)
    "split_type": str,             # "push"
    "muscle_groups": list,
    "exercises": list,
    "warnings": list,
    "validation_warnings": list
}
```

## API Contracts

No API changes. Variation is automatic and internal.

## Component Hierarchy

```
suggest()
├── Build variant tracking map
├── For each day in split:
│   ├── Determine variant group and index
│   ├── Get previously used lower-tier IDs for this group
│   └── build_workout_day(excluded_lower_tier_ids=...)
│       └── selector.select_for_muscle_group(excluded_exercise_ids=...)
│           ├── Phase 0: S+/S selection (unchanged, ignores exclusions)
│           ├── Phase 1: Sub-region fill (respects exclusions)
│           └── Phase 2: Volume fill (respects exclusions)
└── Return workouts with variant field
```

## Testing Strategy

1. **Unit tests** (Phase 4):
   - Variant grouping logic
   - Exercise exclusion in selector
   - Top-tier preservation
   - Sub-region coverage under exclusions

2. **Integration tests**:
   - Full 6-day PPL generation
   - Full 3-day Full Body generation
   - Equipment-constrained scenarios

3. **Manual verification**:
   - Generate workouts and visually confirm variation
   - Check exercise tier distribution

## Edge Cases to Handle

| Case | Handling |
|------|----------|
| Insufficient exercises for variation | Use same exercises, log warning |
| Single variant (5-day PPL) | No exclusions applied |
| Limited equipment | Graceful degradation |
| Beginner with low volume | Accept minimal variation |
| All available exercises are S+/S | No variation possible, identical workouts |

## Implementation Order

1. Phase 1 - Split configuration (data changes only, no logic changes)
2. Phase 2 - ExerciseSelector exclusion parameter
3. Phase 3 - suggest() orchestration with variant tracking
4. Phase 4 - Tests

Each phase can be tested independently before proceeding.
