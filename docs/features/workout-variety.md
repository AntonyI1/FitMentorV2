# Workout Variety - Feature Document

## Overview

Enhance workout generation to provide greater exercise variety and proper volume per muscle group. Each muscle group should be hit multiple times per workout based on experience level, following Jeff Nippard-style programming principles. Gender-specific adjustments for glute training.

## User Stories

1. As an advanced user, I want each muscle group hit 3x per workout for maximum hypertrophy stimulus
2. As an intermediate user, I want each muscle group hit 2x per workout for balanced growth
3. As a beginner, I want each muscle group hit 1-2x per workout to build foundation without overtraining
4. As a female user, I want additional glute focus in my lower body workouts
5. As a male user, I want lower body workouts without dedicated glute isolation

## Acceptance Criteria

1. **Exercise Volume by Experience**
   - Beginner: 1-2 exercises per muscle group per workout
   - Intermediate: 2 exercises per muscle group per workout
   - Advanced: 3 exercises per muscle group per workout

2. **Push Day Coverage** (example)
   - Chest: 2-3 exercises (beginner: 1-2)
   - Shoulders: 2-3 exercises (beginner: 1-2)
   - Triceps: 2-3 exercises (beginner: 1-2)

3. **Gender-Specific Programming**
   - Female: Include glute-focused exercises (hip thrusts, glute bridges, cable kickbacks)
   - Male: No dedicated glute isolation, hip hinge movements sufficient

4. **Exercise Variety**
   - No duplicate exercises within a workout
   - Mix of compound and isolation movements
   - Different movement patterns (e.g., incline + flat + fly for chest)

## Technical Requirements

### Exercise Database Expansion

Add exercises to reach better coverage:

**Chest (target: 10+ exercises)**
- Add: Machine Chest Press, Decline Press, Pec Deck

**Back (target: 10+ exercises)**
- Add: T-Bar Row, Meadows Row, Straight Arm Pulldown, Chest Supported Row

**Legs (target: 15+ exercises)**
- Add: Hack Squat, Sissy Squat, Nordic Curl, Good Morning
- Add glutes: Hip Thrust, Glute Bridge, Cable Kickback, Sumo Deadlift

**Shoulders (target: 8+ exercises)**
- Add: Arnold Press, Machine Shoulder Press, Upright Row

**Biceps (target: 6+ exercises)**
- Add: Preacher Curl, Incline Dumbbell Curl, Cable Curl

**Triceps (target: 6+ exercises)**
- Add: Skull Crusher, Dip (tricep focus), Cable Overhead Extension

**Core (target: 5+ exercises)**
- Add: Hanging Leg Raise, Ab Wheel, Decline Sit-up

### Volume Configuration

```python
EXERCISES_PER_MUSCLE = {
    "beginner": {
        "compound_primary": 1,    # Main compound lift
        "compound_secondary": 1,  # Secondary compound (if available)
        "isolation": 0,           # Optional isolation
    },
    "intermediate": {
        "compound_primary": 1,
        "compound_secondary": 1,
        "isolation": 1,           # Add isolation work
    },
    "advanced": {
        "compound_primary": 1,
        "compound_secondary": 1,
        "isolation": 1,
        "extra": 1,               # Additional variety
    },
}
```

### Gender-Specific Logic

```python
# In workout generation
if gender == "female" and "legs" in muscle_groups:
    # Add glute-focused exercises
    add_glute_exercises(workout, experience_level)
elif gender == "male" and "legs" in muscle_groups:
    # Standard leg work, no glute isolation
    pass
```

### Updated Split Logic

Each muscle group on a given day should receive:
- Beginner: 1-2 exercises total
- Intermediate: 2 exercises total
- Advanced: 3 exercises total

Example Advanced Push Day:
```
Chest (3x):
  1. Barbell Bench Press (compound)
  2. Incline Dumbbell Press (compound)
  3. Cable Fly (isolation)

Shoulders (3x):
  1. Overhead Press (compound)
  2. Lateral Raise (isolation)
  3. Rear Delt Fly (isolation)

Triceps (3x):
  1. Close Grip Bench (compound)
  2. Tricep Pushdown (isolation)
  3. Overhead Extension (isolation)
```

## Dependencies

- `src/backend/models/exercises.py` - Exercise database
- `src/backend/models/workout_suggester.py` - Selection logic

## Edge Cases

1. **Limited equipment**: Fall back to fewer exercises if equipment restricts options
2. **Bodyweight only**: May not reach 3x per muscle group, use what's available
3. **No glute equipment (female)**: Use bodyweight alternatives (glute bridge, lunge variations)

## Exercise Schema Update

Add `gender_focus` field to flag glute exercises:
```python
{
    "id": 39,
    "name": "Barbell Hip Thrust",
    "muscle_group": "glutes",
    "equipment": ["barbell", "bench"],
    "type": "compound",
    "gender_focus": "female",  # or None for neutral
    ...
}
```
