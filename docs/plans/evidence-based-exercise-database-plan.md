# Implementation Plan: Evidence-Based Exercise Database

## Phase 1: Data Model Foundation

### 1.1 Create package structure
- Create `src/backend/models/exercise_data/` directory
- Create `__init__.py` with aggregation logic and constants

### 1.2 Define constants and enums
In `__init__.py`:
```python
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

NIPPARD_TIERS = ["S+", "S", "A+", "A", "B+", "B", "C", "D"]

TIER_RANK = {"S+": 8, "S": 7, "A+": 6, "A": 5, "B+": 4, "B": 3, "C": 2, "D": 1, None: 0}
```

---

## Phase 2: Chest Exercises Module

### 2.1 Create `chest.py`
Extract 24 chest exercises from PDF:
- Upper chest (8 exercises): Incline Barbell Bench Press, Incline Dumbbell Press, Low-to-High Cable Fly, Incline Dumbbell Fly, Seated Cable Fly (Low Position), Incline Smith Machine Press, Reverse-Grip Bench Press, Landmine Press
- Mid chest (10 exercises): Machine Chest Press, Flat Barbell Bench Press, Flat Dumbbell Press, Seated Cable Fly (Mid Position), Pec Deck Machine, Cable Crossover (Mid Height), Flat Dumbbell Fly, Push-Ups (Standard), Deficit Push-Ups
- Lower chest (8 exercises): Chest Dips, Weighted Dips, Decline Barbell Bench Press, Decline Dumbbell Press, High-to-Low Cable Fly, Decline Push-Ups, Decline Dumbbell Fly, Dip Machine (Assisted)

### 2.2 Data format per exercise
```python
{
    "id": "incline-barbell-bench-press",
    "name": "Incline Barbell Bench Press",
    "muscle_group": "chest",
    "sub_region": "upper_chest",
    "difficulty": "medium",
    "equipment": ["barbell", "bench", "rack"],
    "targets": ["upper_pec", "anterior_deltoid", "triceps"],
    "type": "compound",
    "nippard_tier": "A",
    "research_notes": "EMG peaks at 30° incline (~30% MVIC)",
    "rest": 120
}
```

---

## Phase 3: Arms Exercises Module

### 3.1 Create `arms.py`
Extract 24 arm exercises from PDF:
- Biceps short head (8 exercises): Preacher Curl, Concentration Curl, Wide-Grip Barbell Curl, Wide-Grip Cable Curl, Spider Curl, EZ Bar Curl (Wide Grip), Machine Preacher Curl, No Money Curl
- Biceps long head (8 exercises): Bayesian Cable Curl, Incline Dumbbell Curl, Drag Curl, Hammer Curl, Chin-Up, Lying Flat Bench Curl, Narrow-Grip EZ Bar Curl, Overhead Cable Curl
- Triceps lateral/medial (8 exercises): Cable Pushdown (Rope), Cable Pushdown (Straight Bar), Reverse-Grip Pushdown, Close-Grip Bench Press, Diamond Push-Ups, Bench Dips, Tricep Kickback (Cable), JM Press
- Triceps long head (7 exercises): Overhead Cable Extension (Straight Bar), Skull Crushers, Dumbbell Overhead Extension, Cable Overhead Extension (Rope), Incline Dumbbell Kickback, Weighted Dips (Upright), Katana Cable Extension

---

## Phase 4: Shoulders Exercises Module

### 4.1 Create `shoulders.py`
Extract 26 shoulder exercises from PDF:
- Front delt (8 exercises): Machine Shoulder Press, Seated Dumbbell Overhead Press, Standing Barbell Overhead Press, Dumbbell Overhead Press (Standing), Arnold Press, Incline Bench Press, Front Raise, Push-Up
- Side delt (10 exercises): Single-Arm Cable Lateral Raise, Cable Y-Raise, Behind-Back Cuffed Cable Lateral Raise, Cross-Body Cable Lateral Raise, Lean-In Dumbbell Lateral Raise, Standing Dumbbell Lateral Raise, Arnold-Style Side-Lying Raise, Atlantis Standing Machine Lateral Raise, Upright Row, 45-Degree Incline Row
- Rear delt (8 exercises): Reverse Cable Crossover, Reverse Pec Deck, Lying Incline Rear Delt Fly, Rope Face Pull, Seated Rear Lateral Raise, 45-Degree Incline Row, Bent-Over Reverse Dumbbell Fly, Chest-Supported Row

---

## Phase 5: Back Exercises Module

### 5.1 Create `back.py`
Extract 22 back exercises from PDF:
- Upper back (10 exercises): I-Y-T Raises, Face Pulls, Bent-Over Row (Wide Grip), Chest-Supported Row (Wide, High Pull), Inverted Row, Seated Cable Row (Wide Grip), Barbell Shrugs, Cable Shrugs, Cable Y-Raise, Reverse Pec Deck
- Lats (11 exercises): Pull-Ups, Chin-Ups, Lat Pulldown, Single-Arm Lat Pulldown, Chest-Supported Row (Neutral Grip), Seated Cable Row (Close Grip), Single-Arm Dumbbell Row, Bent-Over Row (Underhand), Straight-Arm Pulldown, Dumbbell Pullover, Kroc Row
- Lower back (9 exercises): Conventional Deadlift, Romanian Deadlift, 45-Degree Back Extension, Prone Lumbar Extension, Good Mornings, Superman Hold, Bird Dog, Glute Bridge, Jefferson Curl

---

## Phase 6: Legs Exercises Module

### 6.1 Create `legs.py`
Extract 26 leg exercises from PDF:
- Quadriceps (12 exercises): Barbell Back Squat, Barbell Front Squat, Hack Squat, Pendulum Squat, Smith Machine Squat, Leg Extension, Bulgarian Split Squat, 45-Degree Leg Press, Goblet Squat, Reverse Nordic Curl, Sissy Squat, Walking Lunges (Short Steps)
- Hamstrings (9 exercises): Seated Leg Curl, Romanian Deadlift, Nordic Hamstring Curl, Glute-Ham Raise, Lying/Prone Leg Curl, Stiff-Leg Deadlift, Single-Leg RDL, Stability Ball Hamstring Curl, Good Mornings
- Glutes (14 exercises): Barbell Hip Thrust, Walking Lunges (Long Steps), Machine Hip Abduction, Step-Ups, Deep Back Squat, Cable Kickback, Bulgarian Split Squat, Machine Hip Thrust, Single-Leg Hip Thrust, Glute Bridge, Cable Pull-Through, Side-Lying Hip Abduction, Lateral Band Walks, Reverse Lunge

---

## Phase 7: Query Interface

### 7.1 Create `exercise_query.py`
```python
def query_exercises(
    muscle_group=None,
    sub_region=None,
    equipment=None,
    max_difficulty=None,
    min_tier=None,
    exercise_type=None
) -> list[dict]
```

Logic:
1. Start with all exercises
2. Filter by each non-None parameter
3. For equipment: exercise equipment must be subset of available
4. For difficulty: map easy=1, medium=2, hard=3; filter <= max
5. For tier: use TIER_RANK mapping; filter >= min
6. Return sorted by tier (highest first), then by name

### 7.2 Convenience functions
- `get_top_exercises(muscle_group, n=5)` - returns top N by tier
- `get_exercises_for_equipment_set(equipment_set)` - constraint-based
- `get_compound_exercises(muscle_group)` - compounds only
- `get_isolation_exercises(sub_region)` - isolations only

---

## Phase 8: Integration

### 8.1 Update `exercises.py`
- Import all exercises from `exercise_data`
- Maintain backward-compatible functions
- Add legacy ID mapping for old integer IDs

### 8.2 Update `workout_suggester.py`
- Use `query_exercises()` for exercise selection
- Prioritize S-tier and A-tier exercises for compounds
- Use tier rankings in selection algorithm

---

## Phase 9: Testing

### 9.1 Create `tests/test_exercise_database.py`
- Test total exercise count matches expected
- Test each muscle group has correct sub-regions
- Test equipment filtering works correctly
- Test tier ranking order is correct
- Test backward compatibility with old IDs
- Spot-check specific exercises against PDF source

---

## Complexity Estimate

**Medium-High**

- ~120 exercises to manually transcribe with accurate data
- Research notes parsing requires attention to detail
- Backward compatibility adds constraints
- Testing requires verification against source document

---

## Files Summary

| Action | File |
|--------|------|
| Create | `src/backend/models/exercise_data/__init__.py` |
| Create | `src/backend/models/exercise_data/chest.py` |
| Create | `src/backend/models/exercise_data/arms.py` |
| Create | `src/backend/models/exercise_data/shoulders.py` |
| Create | `src/backend/models/exercise_data/back.py` |
| Create | `src/backend/models/exercise_data/legs.py` |
| Create | `src/backend/models/exercise_query.py` |
| Modify | `src/backend/models/exercises.py` |
| Modify | `src/backend/models/workout_suggester.py` |
| Create | `tests/test_exercise_database.py` |
