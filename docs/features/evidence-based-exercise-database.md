# Evidence-Based Exercise Database

## Overview

Replace the current 65-exercise database with a comprehensive 100+ exercise database sourced from Jeff Nippard's evidence-based recommendations and EMG research. Each exercise includes scientific tier rankings, research citations, and detailed muscle targeting information that enables intelligent workout generation.

## User Stories

1. As a user, I want exercises selected based on scientific effectiveness rankings so my workouts produce optimal results.
2. As a user, I want exercises filtered by my available equipment so I get workouts I can actually perform.
3. As a user, I want exercises matched to my experience level so I progress safely.
4. As a user, I want to target specific muscle sub-regions (e.g., upper chest, long head triceps) for balanced development.
5. As a workout generator, I need to prioritize S-tier exercises in compound movements and use research-backed programming principles.

## Acceptance Criteria

- [x] Database contains 147 exercises (exceeds 100+ target)
- [x] Each exercise has: name, difficulty, equipment, muscle group, sub-region, targets, and research notes
- [x] Nippard tier rankings (S+ through D) are parsed and queryable
- [x] Query interface supports filtering by: muscle group, sub-region, equipment, difficulty, tier ranking
- [x] Equipment constraint queries return only exercises possible with available equipment
- [x] All 5 major muscle groups covered: chest, arms, shoulders, back, legs
- [x] Sub-regions properly mapped: 16 total (3 chest, 4 arms, 3 shoulders, 3 back, 3 legs)
- [ ] Validation tests confirm data integrity against source PDF
- [x] Backward compatible with existing workout_suggester.py API

## Technical Requirements

### Data Model

```python
# Exercise schema
{
    "id": str,                    # Slug: "incline-barbell-bench-press"
    "name": str,                  # "Incline Barbell Bench Press"
    "muscle_group": str,          # chest, arms, shoulders, back, legs
    "sub_region": str,            # upper_chest, biceps_long_head, etc.
    "difficulty": str,            # easy, medium, hard
    "equipment": [str],           # ["barbell", "bench", "rack"]
    "targets": [str],             # ["upper_pec", "anterior_deltoid", "triceps"]
    "type": str,                  # compound, isolation
    "nippard_tier": str | None,   # S+, S, A+, A, B+, B, C, D, or None
    "research_notes": str,        # Original research notes from PDF
    "rest": int                   # Rest seconds (inferred from type/difficulty)
}
```

### Equipment Mapping

Canonical equipment values:
- `bodyweight` - no equipment
- `dumbbell` - dumbbells
- `barbell` - standard barbell
- `barbell_ez` - EZ curl bar
- `bench` - flat/adjustable bench
- `rack` - squat rack / power rack
- `cable` - cable machine / pulley system
- `machine` - dedicated machine (leg press, pec deck, etc.)
- `pullup_bar` - pull-up bar

### Sub-Region Mapping

| Muscle Group | Sub-Regions |
|--------------|-------------|
| chest | upper_chest, mid_chest, lower_chest |
| arms | biceps_short_head, biceps_long_head, triceps_lateral_medial, triceps_long_head |
| shoulders | front_delt, side_delt, rear_delt |
| back | upper_back, lats, lower_back |
| legs | quadriceps, hamstrings, glutes |

### API Functions

```python
def get_all_exercises() -> list[dict]
def get_exercises_by_muscle_group(muscle_group: str) -> list[dict]
def get_exercises_by_sub_region(sub_region: str) -> list[dict]
def get_exercises_by_equipment(equipment_list: list[str]) -> list[dict]
def get_exercises_by_difficulty(difficulty: str) -> list[dict]
def get_exercises_by_tier(min_tier: str) -> list[dict]
def get_exercise_by_id(exercise_id: str) -> dict | None
def query_exercises(
    muscle_group: str = None,
    sub_region: str = None,
    equipment: list[str] = None,
    max_difficulty: str = None,
    min_tier: str = None,
    exercise_type: str = None
) -> list[dict]
```

### Files to Create/Modify

**New Files:**
- `src/backend/models/exercise_data/chest.py` - Chest exercises (24 exercises)
- `src/backend/models/exercise_data/arms.py` - Arms exercises (24 exercises)
- `src/backend/models/exercise_data/shoulders.py` - Shoulder exercises (26 exercises)
- `src/backend/models/exercise_data/back.py` - Back exercises (22 exercises)
- `src/backend/models/exercise_data/legs.py` - Leg exercises (26 exercises)
- `src/backend/models/exercise_data/__init__.py` - Aggregates all exercises
- `src/backend/models/exercise_query.py` - Query interface
- `tests/test_exercise_database.py` - Validation tests

**Modified Files:**
- `src/backend/models/exercises.py` - Import from new modules, maintain backward compatibility
- `src/backend/models/workout_suggester.py` - Use new query interface and tier rankings

## Dependencies

- `src/backend/models/exercises.py` - Current exercise database (will be replaced)
- `src/backend/models/workout_suggester.py` - Uses exercise database
- `src/backend/app.py` - Exposes `/api/exercises` endpoint

## Edge Cases and Error States

1. **Unknown equipment**: If query includes equipment not in canonical list, raise ValidationError
2. **Empty result set**: Return empty list, don't raise error
3. **Invalid tier**: If tier not in valid set, raise ValidationError
4. **Missing tier**: Many exercises don't have Nippard tier; filter should treat None as "unranked"
5. **Backward compatibility**: Old integer IDs must still work via get_exercise_by_id
6. **Case sensitivity**: All queries should be case-insensitive
