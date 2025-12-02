# Workout Variety - Implementation Plan

## Phase 1: Expand Exercise Database

**File:** `src/backend/models/exercises.py`

**Add exercises:**

```python
# Chest additions (3)
{"id": 39, "name": "Machine Chest Press", "muscle_group": "chest", ...}
{"id": 40, "name": "Decline Dumbbell Press", "muscle_group": "chest", ...}
{"id": 41, "name": "Pec Deck", "muscle_group": "chest", ...}

# Back additions (4)
{"id": 42, "name": "T-Bar Row", "muscle_group": "back", ...}
{"id": 43, "name": "Chest Supported Row", "muscle_group": "back", ...}
{"id": 44, "name": "Straight Arm Pulldown", "muscle_group": "back", ...}
{"id": 45, "name": "Inverted Row", "muscle_group": "back", ...}

# Legs additions (4)
{"id": 46, "name": "Hack Squat", "muscle_group": "legs", ...}
{"id": 47, "name": "Good Morning", "muscle_group": "legs", ...}
{"id": 48, "name": "Sissy Squat", "muscle_group": "legs", ...}
{"id": 49, "name": "Nordic Curl", "muscle_group": "legs", ...}

# Glutes (4) - new muscle group
{"id": 50, "name": "Barbell Hip Thrust", "muscle_group": "glutes", ...}
{"id": 51, "name": "Glute Bridge", "muscle_group": "glutes", ...}
{"id": 52, "name": "Cable Kickback", "muscle_group": "glutes", ...}
{"id": 53, "name": "Sumo Deadlift", "muscle_group": "glutes", ...}

# Shoulders additions (3)
{"id": 54, "name": "Arnold Press", "muscle_group": "shoulders", ...}
{"id": 55, "name": "Machine Shoulder Press", "muscle_group": "shoulders", ...}
{"id": 56, "name": "Upright Row", "muscle_group": "shoulders", ...}

# Biceps additions (3)
{"id": 57, "name": "Preacher Curl", "muscle_group": "biceps", ...}
{"id": 58, "name": "Incline Dumbbell Curl", "muscle_group": "biceps", ...}
{"id": 59, "name": "Cable Curl", "muscle_group": "biceps", ...}

# Triceps additions (3)
{"id": 60, "name": "Skull Crusher", "muscle_group": "triceps", ...}
{"id": 61, "name": "Tricep Dip", "muscle_group": "triceps", ...}
{"id": 62, "name": "Cable Overhead Extension", "muscle_group": "triceps", ...}

# Core additions (3)
{"id": 63, "name": "Hanging Leg Raise", "muscle_group": "core", ...}
{"id": 64, "name": "Ab Wheel Rollout", "muscle_group": "core", ...}
{"id": 65, "name": "Decline Sit-up", "muscle_group": "core", ...}
```

Total: 27 new exercises (38 → 65)

## Phase 2: Update Workout Suggester Volume Logic

**File:** `src/backend/models/workout_suggester.py`

**Add volume configuration:**

```python
VOLUME_PER_MUSCLE = {
    "beginner": 1,      # 1-2 exercises per muscle group
    "intermediate": 2,  # 2 exercises per muscle group
    "advanced": 3,      # 3 exercises per muscle group
}
```

**Update `select_exercises_for_muscle_group()`:**
- Accept experience level parameter
- Return appropriate number based on VOLUME_PER_MUSCLE
- Prioritize: compound first, then isolation
- Ensure variety (different movement patterns)

**Update `build_workout_day()`:**
- Pass experience to exercise selection
- Use VOLUME_PER_MUSCLE[experience] as count

## Phase 3: Add Gender-Specific Glute Logic

**File:** `src/backend/models/workout_suggester.py`

**Update splits to include glutes for females:**

```python
# Modify SPLITS to have gender variants or handle dynamically
def get_muscle_groups_for_day(day_info, gender):
    groups = day_info["muscle_groups"].copy()
    if gender == "female" and "legs" in groups:
        groups.append("glutes")
    return groups
```

**Update `build_workout_day()`:**
- Check gender
- If female + legs day: add glute exercises
- If male: skip glute isolation (hip hinge covers glutes)

## Phase 4: Update Exercise Selection Algorithm

**File:** `src/backend/models/workout_suggester.py`

**New selection logic:**

```python
def select_exercises_for_muscle_group(muscle_group, available, goal, experience):
    count = VOLUME_PER_MUSCLE[experience]

    muscle_exercises = [e for e in available if e["muscle_group"] == muscle_group]
    compounds = [e for e in muscle_exercises if e["type"] == "compound"]
    isolations = [e for e in muscle_exercises if e["type"] == "isolation"]

    selected = []

    # Always start with compounds
    for ex in compounds:
        if len(selected) >= count:
            break
        if ex not in selected:
            selected.append(ex)

    # Fill remaining with isolations
    for ex in isolations:
        if len(selected) >= count:
            break
        if ex not in selected:
            selected.append(ex)

    return selected[:count]
```

## Phase 5: Testing

**Manual tests:**

1. Generate beginner plan - verify 1-2 exercises per muscle
2. Generate intermediate plan - verify 2 exercises per muscle
3. Generate advanced plan - verify 3 exercises per muscle
4. Generate female plan - verify glute exercises on leg days
5. Generate male plan - verify no glute isolation
6. Test with limited equipment - verify graceful fallback

## Files to Modify

| File | Action |
|------|--------|
| `src/backend/models/exercises.py` | Add 27 exercises |
| `src/backend/models/workout_suggester.py` | Update volume logic, add gender handling |

## Complexity Estimate

**Medium** - Adding exercises is straightforward. Logic changes to workout suggester are moderate but self-contained.
