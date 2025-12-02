"""Exercise database with 65 exercises across 8 muscle groups."""

EXERCISES = [
    # Chest (11 exercises)
    {"id": 1, "name": "Barbell Bench Press", "muscle_group": "chest", "subcategory": "mid_chest", "equipment": ["barbell", "bench", "rack"], "difficulty": "intermediate", "type": "compound", "category": "flat_press", "rest": 120},
    {"id": 2, "name": "Dumbbell Bench Press", "muscle_group": "chest", "subcategory": "mid_chest", "equipment": ["dumbbell", "bench"], "difficulty": "beginner", "type": "compound", "category": "flat_press", "rest": 120},
    {"id": 3, "name": "Incline Barbell Press", "muscle_group": "chest", "subcategory": "upper_chest", "equipment": ["barbell", "bench", "rack"], "difficulty": "intermediate", "type": "compound", "category": "incline_press", "rest": 120},
    {"id": 4, "name": "Incline Dumbbell Press", "muscle_group": "chest", "subcategory": "upper_chest", "equipment": ["dumbbell", "bench"], "difficulty": "beginner", "type": "compound", "category": "incline_press", "rest": 120},
    {"id": 5, "name": "Cable Fly", "muscle_group": "chest", "subcategory": "mid_chest", "equipment": ["cable"], "difficulty": "beginner", "type": "isolation", "category": "chest_fly", "rest": 90},
    {"id": 6, "name": "Dumbbell Fly", "muscle_group": "chest", "subcategory": "mid_chest", "equipment": ["dumbbell", "bench"], "difficulty": "beginner", "type": "isolation", "category": "chest_fly", "rest": 90},
    {"id": 7, "name": "Chest Dip", "muscle_group": "chest", "subcategory": "lower_chest", "equipment": ["bodyweight"], "difficulty": "intermediate", "type": "compound", "category": "dip", "rest": 120},
    {"id": 8, "name": "Push-Up", "muscle_group": "chest", "subcategory": "mid_chest", "equipment": ["bodyweight"], "difficulty": "beginner", "type": "compound", "category": "flat_press", "rest": 90},
    {"id": 39, "name": "Machine Chest Press", "muscle_group": "chest", "subcategory": "mid_chest", "equipment": ["machine"], "difficulty": "beginner", "type": "compound", "category": "flat_press", "rest": 90},
    {"id": 40, "name": "Decline Dumbbell Press", "muscle_group": "chest", "subcategory": "lower_chest", "equipment": ["dumbbell", "bench"], "difficulty": "intermediate", "type": "compound", "category": "decline_press", "rest": 120},
    {"id": 41, "name": "Pec Deck", "muscle_group": "chest", "subcategory": "mid_chest", "equipment": ["machine"], "difficulty": "beginner", "type": "isolation", "category": "chest_fly", "rest": 60},

    # Back (10 exercises)
    {"id": 9, "name": "Pull-Up", "muscle_group": "back", "subcategory": "lats", "equipment": ["pullup_bar"], "difficulty": "intermediate", "type": "compound", "category": "vertical_pull", "rest": 120},
    {"id": 10, "name": "Lat Pulldown", "muscle_group": "back", "subcategory": "lats", "equipment": ["cable"], "difficulty": "beginner", "type": "compound", "category": "vertical_pull", "rest": 90},
    {"id": 11, "name": "Barbell Row", "muscle_group": "back", "subcategory": "mid_back", "equipment": ["barbell"], "difficulty": "intermediate", "type": "compound", "category": "horizontal_pull", "rest": 120},
    {"id": 12, "name": "Dumbbell Row", "muscle_group": "back", "subcategory": "mid_back", "equipment": ["dumbbell", "bench"], "difficulty": "beginner", "type": "compound", "category": "horizontal_pull", "rest": 90},
    {"id": 13, "name": "Seated Cable Row", "muscle_group": "back", "subcategory": "mid_back", "equipment": ["cable"], "difficulty": "beginner", "type": "compound", "category": "horizontal_pull", "rest": 90},
    {"id": 14, "name": "Face Pull", "muscle_group": "back", "subcategory": "rear_delt", "equipment": ["cable"], "difficulty": "beginner", "type": "isolation", "category": "isolation", "rest": 60},
    {"id": 42, "name": "T-Bar Row", "muscle_group": "back", "subcategory": "mid_back", "equipment": ["barbell"], "difficulty": "intermediate", "type": "compound", "category": "horizontal_pull", "rest": 120},
    {"id": 43, "name": "Chest Supported Row", "muscle_group": "back", "subcategory": "mid_back", "equipment": ["dumbbell", "bench"], "difficulty": "beginner", "type": "compound", "category": "horizontal_pull", "rest": 90},
    {"id": 44, "name": "Straight Arm Pulldown", "muscle_group": "back", "subcategory": "lats", "equipment": ["cable"], "difficulty": "beginner", "type": "isolation", "category": "isolation", "rest": 60},
    {"id": 45, "name": "Inverted Row", "muscle_group": "back", "subcategory": "mid_back", "equipment": ["bodyweight"], "difficulty": "beginner", "type": "compound", "category": "horizontal_pull", "rest": 90},

    # Legs (15 exercises)
    {"id": 15, "name": "Barbell Back Squat", "muscle_group": "legs", "subcategory": "quads", "equipment": ["barbell", "rack"], "difficulty": "intermediate", "type": "compound", "category": "squat", "rest": 180},
    {"id": 16, "name": "Goblet Squat", "muscle_group": "legs", "subcategory": "quads", "equipment": ["dumbbell"], "difficulty": "beginner", "type": "compound", "category": "squat", "rest": 120},
    {"id": 17, "name": "Leg Press", "muscle_group": "legs", "subcategory": "quads", "equipment": ["machine"], "difficulty": "beginner", "type": "compound", "category": "squat", "rest": 120},
    {"id": 18, "name": "Romanian Deadlift", "muscle_group": "legs", "subcategory": "hamstrings", "equipment": ["barbell"], "difficulty": "intermediate", "type": "compound", "category": "hip_hinge", "rest": 120},
    {"id": 19, "name": "Dumbbell Romanian Deadlift", "muscle_group": "legs", "subcategory": "hamstrings", "equipment": ["dumbbell"], "difficulty": "beginner", "type": "compound", "category": "hip_hinge", "rest": 120},
    {"id": 20, "name": "Leg Curl", "muscle_group": "legs", "subcategory": "hamstrings", "equipment": ["machine"], "difficulty": "beginner", "type": "isolation", "category": "hamstring_iso", "rest": 90},
    {"id": 21, "name": "Leg Extension", "muscle_group": "legs", "subcategory": "quads", "equipment": ["machine"], "difficulty": "beginner", "type": "isolation", "category": "quad_iso", "rest": 90},
    {"id": 22, "name": "Walking Lunge", "muscle_group": "legs", "subcategory": "quads", "equipment": ["dumbbell"], "difficulty": "beginner", "type": "compound", "category": "unilateral", "rest": 90},
    {"id": 23, "name": "Bulgarian Split Squat", "muscle_group": "legs", "subcategory": "quads", "equipment": ["dumbbell", "bench"], "difficulty": "intermediate", "type": "compound", "category": "unilateral", "rest": 90},
    {"id": 24, "name": "Calf Raise", "muscle_group": "legs", "subcategory": "calves", "equipment": ["machine"], "difficulty": "beginner", "type": "isolation", "category": "calf", "rest": 60},
    {"id": 25, "name": "Bodyweight Squat", "muscle_group": "legs", "subcategory": "quads", "equipment": ["bodyweight"], "difficulty": "beginner", "type": "compound", "category": "squat", "rest": 60},
    {"id": 46, "name": "Hack Squat", "muscle_group": "legs", "subcategory": "quads", "equipment": ["machine"], "difficulty": "beginner", "type": "compound", "category": "squat", "rest": 120},
    {"id": 47, "name": "Good Morning", "muscle_group": "legs", "subcategory": "hamstrings", "equipment": ["barbell", "rack"], "difficulty": "intermediate", "type": "compound", "category": "hip_hinge", "rest": 120},
    {"id": 48, "name": "Sissy Squat", "muscle_group": "legs", "subcategory": "quads", "equipment": ["bodyweight"], "difficulty": "intermediate", "type": "isolation", "category": "quad_iso", "rest": 90},
    {"id": 49, "name": "Nordic Curl", "muscle_group": "legs", "subcategory": "hamstrings", "equipment": ["bodyweight"], "difficulty": "advanced", "type": "isolation", "category": "hamstring_iso", "rest": 120},

    # Glutes (5 exercises) - female focus
    {"id": 50, "name": "Barbell Hip Thrust", "muscle_group": "glutes", "subcategory": "glutes", "equipment": ["barbell", "bench"], "difficulty": "intermediate", "type": "compound", "category": "hip_thrust", "rest": 120},
    {"id": 51, "name": "Glute Bridge", "muscle_group": "glutes", "subcategory": "glutes", "equipment": ["bodyweight"], "difficulty": "beginner", "type": "compound", "category": "hip_thrust", "rest": 60},
    {"id": 52, "name": "Cable Kickback", "muscle_group": "glutes", "subcategory": "glutes", "equipment": ["cable"], "difficulty": "beginner", "type": "isolation", "category": "glute_iso", "rest": 60},
    {"id": 53, "name": "Sumo Deadlift", "muscle_group": "glutes", "subcategory": "glutes", "equipment": ["barbell"], "difficulty": "intermediate", "type": "compound", "category": "hip_hinge", "rest": 150},
    {"id": 54, "name": "Dumbbell Hip Thrust", "muscle_group": "glutes", "subcategory": "glutes", "equipment": ["dumbbell", "bench"], "difficulty": "beginner", "type": "compound", "category": "hip_thrust", "rest": 90},

    # Shoulders (8 exercises)
    {"id": 26, "name": "Overhead Press", "muscle_group": "shoulders", "subcategory": "front_delt", "equipment": ["barbell", "rack"], "difficulty": "intermediate", "type": "compound", "category": "overhead_press", "rest": 120},
    {"id": 27, "name": "Dumbbell Shoulder Press", "muscle_group": "shoulders", "subcategory": "front_delt", "equipment": ["dumbbell", "bench"], "difficulty": "beginner", "type": "compound", "category": "overhead_press", "rest": 120},
    {"id": 28, "name": "Lateral Raise", "muscle_group": "shoulders", "subcategory": "side_delt", "equipment": ["dumbbell"], "difficulty": "beginner", "type": "isolation", "category": "lateral_delt", "rest": 60},
    {"id": 29, "name": "Rear Delt Fly", "muscle_group": "shoulders", "subcategory": "rear_delt", "equipment": ["dumbbell"], "difficulty": "beginner", "type": "isolation", "category": "rear_delt", "rest": 60},
    {"id": 30, "name": "Cable Lateral Raise", "muscle_group": "shoulders", "subcategory": "side_delt", "equipment": ["cable"], "difficulty": "beginner", "type": "isolation", "category": "lateral_delt", "rest": 60},
    {"id": 55, "name": "Arnold Press", "muscle_group": "shoulders", "subcategory": "front_delt", "equipment": ["dumbbell", "bench"], "difficulty": "intermediate", "type": "compound", "category": "overhead_press", "rest": 120},
    {"id": 56, "name": "Machine Shoulder Press", "muscle_group": "shoulders", "subcategory": "front_delt", "equipment": ["machine"], "difficulty": "beginner", "type": "compound", "category": "overhead_press", "rest": 90},
    {"id": 57, "name": "Upright Row", "muscle_group": "shoulders", "subcategory": "side_delt", "equipment": ["barbell"], "difficulty": "intermediate", "type": "compound", "category": "upright_row", "rest": 90},

    # Biceps (6 exercises)
    {"id": 31, "name": "Barbell Curl", "muscle_group": "biceps", "subcategory": "biceps", "equipment": ["barbell"], "difficulty": "beginner", "type": "isolation", "category": "bicep_curl", "rest": 90},
    {"id": 32, "name": "Dumbbell Curl", "muscle_group": "biceps", "subcategory": "biceps", "equipment": ["dumbbell"], "difficulty": "beginner", "type": "isolation", "category": "bicep_curl", "rest": 60},
    {"id": 33, "name": "Hammer Curl", "muscle_group": "biceps", "subcategory": "biceps", "equipment": ["dumbbell"], "difficulty": "beginner", "type": "isolation", "category": "bicep_curl", "rest": 60},
    {"id": 58, "name": "Preacher Curl", "muscle_group": "biceps", "subcategory": "biceps", "equipment": ["barbell", "bench"], "difficulty": "beginner", "type": "isolation", "category": "bicep_curl", "rest": 60},
    {"id": 59, "name": "Incline Dumbbell Curl", "muscle_group": "biceps", "subcategory": "biceps", "equipment": ["dumbbell", "bench"], "difficulty": "beginner", "type": "isolation", "category": "bicep_curl", "rest": 60},
    {"id": 60, "name": "Cable Curl", "muscle_group": "biceps", "subcategory": "biceps", "equipment": ["cable"], "difficulty": "beginner", "type": "isolation", "category": "bicep_curl", "rest": 60},

    # Triceps (6 exercises)
    {"id": 34, "name": "Tricep Pushdown", "muscle_group": "triceps", "subcategory": "triceps", "equipment": ["cable"], "difficulty": "beginner", "type": "isolation", "category": "tricep_extension", "rest": 60},
    {"id": 35, "name": "Overhead Tricep Extension", "muscle_group": "triceps", "subcategory": "triceps", "equipment": ["dumbbell"], "difficulty": "beginner", "type": "isolation", "category": "tricep_extension", "rest": 60},
    {"id": 36, "name": "Close Grip Bench Press", "muscle_group": "triceps", "subcategory": "triceps", "equipment": ["barbell", "bench", "rack"], "difficulty": "intermediate", "type": "compound", "category": "tricep_press", "rest": 120},
    {"id": 61, "name": "Skull Crusher", "muscle_group": "triceps", "subcategory": "triceps", "equipment": ["barbell", "bench"], "difficulty": "intermediate", "type": "isolation", "category": "tricep_extension", "rest": 90},
    {"id": 62, "name": "Tricep Dip", "muscle_group": "triceps", "subcategory": "triceps", "equipment": ["bodyweight"], "difficulty": "intermediate", "type": "compound", "category": "tricep_press", "rest": 90},
    {"id": 63, "name": "Cable Overhead Extension", "muscle_group": "triceps", "subcategory": "triceps", "equipment": ["cable"], "difficulty": "beginner", "type": "isolation", "category": "tricep_extension", "rest": 60},

    # Core (5 exercises)
    {"id": 37, "name": "Plank", "muscle_group": "core", "subcategory": "core", "equipment": ["bodyweight"], "difficulty": "beginner", "type": "isolation", "category": "core", "rest": 60},
    {"id": 38, "name": "Cable Crunch", "muscle_group": "core", "subcategory": "core", "equipment": ["cable"], "difficulty": "beginner", "type": "isolation", "category": "core", "rest": 60},
    {"id": 64, "name": "Hanging Leg Raise", "muscle_group": "core", "subcategory": "core", "equipment": ["pullup_bar"], "difficulty": "intermediate", "type": "isolation", "category": "core", "rest": 60},
    {"id": 65, "name": "Ab Wheel Rollout", "muscle_group": "core", "subcategory": "core", "equipment": ["bodyweight"], "difficulty": "intermediate", "type": "isolation", "category": "core", "rest": 90},
    {"id": 66, "name": "Decline Sit-up", "muscle_group": "core", "subcategory": "core", "equipment": ["bench"], "difficulty": "beginner", "type": "isolation", "category": "core", "rest": 60},
]


def get_all_exercises():
    """Return all exercises."""
    return EXERCISES


def get_exercises_by_muscle_group(muscle_group):
    """Return exercises for a specific muscle group."""
    return [e for e in EXERCISES if e["muscle_group"] == muscle_group]


def get_exercises_by_equipment(equipment_list):
    """Return exercises that can be performed with given equipment."""
    equipment_set = set(equipment_list)
    return [
        e for e in EXERCISES
        if set(e["equipment"]).issubset(equipment_set)
    ]


def get_exercise_by_id(exercise_id):
    """Return a specific exercise by ID."""
    for e in EXERCISES:
        if e["id"] == exercise_id:
            return e
    return None
