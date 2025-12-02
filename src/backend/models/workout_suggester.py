"""Workout plan generator based on user parameters and training principles."""

from models.exercises import get_exercises_by_equipment, EXERCISES

VALID_GENDERS = {"male", "female"}
VALID_GOALS = {"strength", "hypertrophy", "endurance", "weight_loss"}
VALID_EXPERIENCE = {"beginner", "intermediate", "advanced"}
VALID_EQUIPMENT = {"barbell", "dumbbell", "machine", "cable", "bench", "rack", "pullup_bar", "bodyweight"}

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

SPLITS = {
    3: {
        "name": "Full Body 3x/week",
        "days": [
            {"name": "Full Body A", "muscle_groups": ["chest", "back", "legs", "shoulders", "biceps", "triceps", "core"]},
            {"name": "Full Body B", "muscle_groups": ["chest", "back", "legs", "shoulders", "biceps", "triceps", "core"]},
            {"name": "Full Body C", "muscle_groups": ["chest", "back", "legs", "shoulders", "biceps", "triceps", "core"]},
        ],
    },
    4: {
        "name": "Upper/Lower 4x/week",
        "days": [
            {"name": "Upper A", "muscle_groups": ["chest", "back", "shoulders", "biceps", "triceps"]},
            {"name": "Lower A", "muscle_groups": ["legs", "core"]},
            {"name": "Upper B", "muscle_groups": ["chest", "back", "shoulders", "biceps", "triceps"]},
            {"name": "Lower B", "muscle_groups": ["legs", "core"]},
        ],
    },
    5: {
        "name": "Push/Pull/Legs 5x/week",
        "days": [
            {"name": "Push", "muscle_groups": ["chest", "shoulders", "triceps"]},
            {"name": "Pull", "muscle_groups": ["back", "biceps"]},
            {"name": "Legs", "muscle_groups": ["legs", "core"]},
            {"name": "Upper", "muscle_groups": ["chest", "back", "shoulders", "biceps", "triceps"]},
            {"name": "Lower", "muscle_groups": ["legs", "core"]},
        ],
    },
    6: {
        "name": "Push/Pull/Legs 6x/week",
        "days": [
            {"name": "Push A", "muscle_groups": ["chest", "shoulders", "triceps"]},
            {"name": "Pull A", "muscle_groups": ["back", "biceps"]},
            {"name": "Legs A", "muscle_groups": ["legs", "core"]},
            {"name": "Push B", "muscle_groups": ["chest", "shoulders", "triceps"]},
            {"name": "Pull B", "muscle_groups": ["back", "biceps"]},
            {"name": "Legs B", "muscle_groups": ["legs", "core"]},
        ],
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
        raise ValidationError(f"Invalid equipment: {', '.join(invalid_equipment)}. Valid options: {', '.join(VALID_EQUIPMENT)}")

    days = data["days_per_week"]
    if not isinstance(days, int) or days < 3 or days > 6:
        raise ValidationError("days_per_week must be an integer between 3 and 6")

    duration = data.get("session_duration", 60)
    if not isinstance(duration, int) or duration < 30 or duration > 120:
        raise ValidationError("session_duration must be an integer between 30 and 120")


def select_exercises_for_muscle_group(muscle_group, available_exercises, goal, count=2):
    """Select exercises for a muscle group from available exercises."""
    muscle_exercises = [e for e in available_exercises if e["muscle_group"] == muscle_group]

    if not muscle_exercises:
        bodyweight = [e for e in EXERCISES if e["muscle_group"] == muscle_group and "bodyweight" in e["equipment"]]
        muscle_exercises = bodyweight[:count] if bodyweight else []

    compounds = [e for e in muscle_exercises if e["type"] == "compound"]
    isolations = [e for e in muscle_exercises if e["type"] == "isolation"]

    selected = []
    if compounds:
        selected.append(compounds[0])
    if isolations and len(selected) < count:
        selected.append(isolations[0])

    while len(selected) < count and len(selected) < len(muscle_exercises):
        for e in muscle_exercises:
            if e not in selected:
                selected.append(e)
                break

    return selected[:count]


def build_workout_day(day_info, available_exercises, goal_params, experience):
    """Build a single workout day."""
    exercises = []
    volume_mult = EXPERIENCE_MULTIPLIERS[experience]

    exercise_counts = {
        "chest": 2, "back": 2, "legs": 3, "shoulders": 2,
        "biceps": 1, "triceps": 1, "core": 1,
    }

    for muscle_group in day_info["muscle_groups"]:
        count = exercise_counts.get(muscle_group, 2)
        if len(day_info["muscle_groups"]) > 5:
            count = 1

        selected = select_exercises_for_muscle_group(
            muscle_group, available_exercises, goal_params, count
        )

        for exercise in selected:
            sets = max(2, round(goal_params["sets"] * volume_mult))
            rest = exercise.get("rest", goal_params["rest"])

            if exercise["type"] == "isolation":
                rest = min(rest, 90)

            exercises.append({
                "name": exercise["name"],
                "muscle_group": exercise["muscle_group"],
                "sets": sets,
                "reps": goal_params["reps"],
                "rest_seconds": rest,
                "type": exercise["type"],
            })

    return {
        "day": day_info["name"],
        "muscle_groups": day_info["muscle_groups"],
        "exercises": exercises,
    }


def suggest(data):
    """Generate a workout plan based on user parameters."""
    validate_input(data)

    equipment = data["equipment"]
    if "bodyweight" not in equipment:
        equipment = equipment + ["bodyweight"]

    available_exercises = get_exercises_by_equipment(equipment)

    split = SPLITS[data["days_per_week"]]
    goal_params = GOAL_PARAMS[data["goal"]]
    progression = PROGRESSIONS[data["goal"]]

    workouts = []
    for day_info in split["days"]:
        workout = build_workout_day(
            day_info, available_exercises, goal_params, data["experience"]
        )
        workouts.append(workout)

    return {
        "split": {
            "name": split["name"],
            "days": split["days"],
        },
        "workouts": workouts,
        "progression": progression,
        "parameters": {
            "goal": data["goal"],
            "experience": data["experience"],
            "days_per_week": data["days_per_week"],
            "session_duration": data.get("session_duration", 60),
        },
    }
