"""Leg exercises - 35 exercises across 3 sub-regions.

Sub-regions:
- quadriceps: 12 exercises
- hamstrings: 9 exercises
- glutes: 14 exercises

Research note: EMG and hypertrophy research reveals important findings:
- Seated leg curls produce 1.5x more hamstring growth than lying curls
  due to the lengthened position.
- For glutes, a 2023 study found hip thrusts and squats produce equal
  hypertrophy despite hip thrusts showing 2x higher EMG.
- Deep squats (140°) significantly increase glute and adductor growth.
"""

LEG_EXERCISES = [
    # =========================================================================
    # QUADRICEPS - 12 exercises
    # =========================================================================
    {
        "id": "barbell-back-squat",
        "name": "Barbell Back Squat",
        "muscle_group": "legs",
        "sub_region": "quadriceps",
        "difficulty": "medium",
        "equipment": ["barbell", "rack"],
        "targets": ["all_quad_heads", "glutes"],
        "type": "compound",
        "nippard_tier": "S",
        "research_notes": "Nippard S-tier; 2022 study confirms growth in all quad muscles",
        "rest": 180
    },
    {
        "id": "barbell-front-squat",
        "name": "Barbell Front Squat",
        "muscle_group": "legs",
        "sub_region": "quadriceps",
        "difficulty": "hard",
        "equipment": ["barbell", "rack"],
        "targets": ["all_quad_heads", "rectus_femoris"],
        "type": "compound",
        "nippard_tier": "S",
        "research_notes": "Nippard S-tier; upright torso shifts tension to quads",
        "rest": 180
    },
    {
        "id": "hack-squat",
        "name": "Hack Squat",
        "muscle_group": "legs",
        "sub_region": "quadriceps",
        "difficulty": "medium",
        "equipment": ["machine"],
        "targets": ["all_quad_heads"],
        "type": "compound",
        "nippard_tier": "S",
        "research_notes": "Nippard S-tier; 'brilliant quad builder'",
        "rest": 120
    },
    {
        "id": "pendulum-squat",
        "name": "Pendulum Squat",
        "muscle_group": "legs",
        "sub_region": "quadriceps",
        "difficulty": "medium",
        "equipment": ["machine"],
        "targets": ["all_quad_heads"],
        "type": "compound",
        "nippard_tier": "S",
        "research_notes": "Nippard S-tier; natural arc motion",
        "rest": 120
    },
    {
        "id": "smith-machine-squat",
        "name": "Smith Machine Squat",
        "muscle_group": "legs",
        "sub_region": "quadriceps",
        "difficulty": "medium",
        "equipment": ["machine"],
        "targets": ["all_quad_heads"],
        "type": "compound",
        "nippard_tier": "S",
        "research_notes": "Nippard S-tier; safe failure training",
        "rest": 120
    },
    {
        "id": "leg-extension",
        "name": "Leg Extension",
        "muscle_group": "legs",
        "sub_region": "quadriceps",
        "difficulty": "easy",
        "equipment": ["machine"],
        "targets": ["rectus_femoris", "vastus_lateralis", "vastus_medialis"],
        "type": "isolation",
        "nippard_tier": "S",
        "research_notes": "Nippard S-tier; all four heads engaged",
        "rest": 60
    },
    {
        "id": "bulgarian-split-squat",
        "name": "Bulgarian Split Squat",
        "muscle_group": "legs",
        "sub_region": "quadriceps",
        "difficulty": "hard",
        "equipment": ["dumbbell", "bench"],
        "targets": ["vastus_lateralis", "vastus_medialis", "rectus_femoris"],
        "type": "compound",
        "nippard_tier": "A",
        "research_notes": "Nippard A-tier; deep unilateral stretch",
        "rest": 90
    },
    {
        "id": "45-degree-leg-press",
        "name": "45-Degree Leg Press",
        "muscle_group": "legs",
        "sub_region": "quadriceps",
        "difficulty": "medium",
        "equipment": ["machine"],
        "targets": ["vastus_lateralis", "vastus_medialis", "vastus_intermedius"],
        "type": "compound",
        "nippard_tier": "A",
        "research_notes": "Nippard A-tier; narrow stance biases quads",
        "rest": 120
    },
    {
        "id": "goblet-squat",
        "name": "Goblet Squat",
        "muscle_group": "legs",
        "sub_region": "quadriceps",
        "difficulty": "easy",
        "equipment": ["dumbbell"],
        "targets": ["all_quad_heads"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Similar to front squat; excellent for beginners",
        "rest": 90
    },
    {
        "id": "reverse-nordic-curl",
        "name": "Reverse Nordic Curl",
        "muscle_group": "legs",
        "sub_region": "quadriceps",
        "difficulty": "hard",
        "equipment": ["bodyweight"],
        "targets": ["all_quad_heads", "rectus_femoris"],
        "type": "isolation",
        "nippard_tier": "A",
        "research_notes": "Nippard A-tier; deepest quad stretch possible",
        "rest": 90
    },
    {
        "id": "sissy-squat",
        "name": "Sissy Squat",
        "muscle_group": "legs",
        "sub_region": "quadriceps",
        "difficulty": "hard",
        "equipment": ["cable", "bodyweight"],
        "targets": ["rectus_femoris", "vastus_medialis"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "High stretch; knees forward strengthens knees",
        "rest": 90
    },
    {
        "id": "walking-lunges-short",
        "name": "Walking Lunges (Short Steps)",
        "muscle_group": "legs",
        "sub_region": "quadriceps",
        "difficulty": "medium",
        "equipment": ["dumbbell", "barbell"],
        "targets": ["quadriceps"],
        "type": "compound",
        "nippard_tier": "B",
        "research_notes": "B-tier for quads; shorter steps = more quad",
        "rest": 90
    },

    # =========================================================================
    # HAMSTRINGS - 9 exercises
    # =========================================================================
    {
        "id": "seated-leg-curl",
        "name": "Seated Leg Curl",
        "muscle_group": "legs",
        "sub_region": "hamstrings",
        "difficulty": "easy",
        "equipment": ["machine"],
        "targets": ["biceps_femoris", "semitendinosus", "semimembranosus"],
        "type": "isolation",
        "nippard_tier": "S",
        "research_notes": "2021 study: 1.5x more growth than lying curl",
        "rest": 60
    },
    {
        "id": "romanian-deadlift",
        "name": "Romanian Deadlift",
        "muscle_group": "legs",
        "sub_region": "hamstrings",
        "difficulty": "medium",
        "equipment": ["barbell", "dumbbell"],
        "targets": ["biceps_femoris", "semitendinosus", "semimembranosus"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "McAllister 2014: greatest semitendinosus activation",
        "rest": 120
    },
    {
        "id": "nordic-hamstring-curl",
        "name": "Nordic Hamstring Curl",
        "muscle_group": "legs",
        "sub_region": "hamstrings",
        "difficulty": "hard",
        "equipment": ["bodyweight"],
        "targets": ["biceps_femoris", "semitendinosus"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "Highest EMG rise rate (1091.8 nEMG/s); injury prevention",
        "rest": 120
    },
    {
        "id": "glute-ham-raise",
        "name": "Glute-Ham Raise",
        "muscle_group": "legs",
        "sub_region": "hamstrings",
        "difficulty": "hard",
        "equipment": ["machine"],
        "targets": ["biceps_femoris", "semitendinosus", "glutes"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Best overall hamstring activation (McAllister)",
        "rest": 120
    },
    {
        "id": "lying-leg-curl",
        "name": "Lying/Prone Leg Curl",
        "muscle_group": "legs",
        "sub_region": "hamstrings",
        "difficulty": "easy",
        "equipment": ["machine"],
        "targets": ["biceps_femoris", "semitendinosus"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "Equal BF and ST activation; baseline exercise",
        "rest": 60
    },
    {
        "id": "stiff-leg-deadlift",
        "name": "Stiff-Leg Deadlift",
        "muscle_group": "legs",
        "sub_region": "hamstrings",
        "difficulty": "medium",
        "equipment": ["barbell", "dumbbell"],
        "targets": ["all_hamstring_muscles"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Upper-inside hamstring emphasis",
        "rest": 120
    },
    {
        "id": "single-leg-rdl",
        "name": "Single-Leg RDL",
        "muscle_group": "legs",
        "sub_region": "hamstrings",
        "difficulty": "hard",
        "equipment": ["dumbbell"],
        "targets": ["hamstrings", "glute_medius"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Balance challenge; corrects imbalances",
        "rest": 90
    },
    {
        "id": "stability-ball-hamstring-curl",
        "name": "Stability Ball Hamstring Curl",
        "muscle_group": "legs",
        "sub_region": "hamstrings",
        "difficulty": "medium",
        "equipment": ["bodyweight"],
        "targets": ["semitendinosus", "biceps_femoris"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "ACE: higher semitendinosus than prone curl",
        "rest": 60
    },
    {
        "id": "good-mornings",
        "name": "Good Mornings",
        "muscle_group": "legs",
        "sub_region": "hamstrings",
        "difficulty": "medium",
        "equipment": ["barbell"],
        "targets": ["biceps_femoris", "semitendinosus", "erectors"],
        "type": "compound",
        "nippard_tier": "B",
        "research_notes": "B-tier; good RDL alternative",
        "rest": 120
    },

    # =========================================================================
    # GLUTES - 14 exercises
    # =========================================================================
    {
        "id": "barbell-hip-thrust",
        "name": "Barbell Hip Thrust",
        "muscle_group": "legs",
        "sub_region": "glutes",
        "difficulty": "medium",
        "equipment": ["barbell", "bench"],
        "targets": ["gluteus_maximus"],
        "type": "compound",
        "nippard_tier": "A",
        "research_notes": "Nippard A-tier; 2x EMG vs squat; equal hypertrophy",
        "rest": 120
    },
    {
        "id": "walking-lunges-long",
        "name": "Walking Lunges (Long Steps)",
        "muscle_group": "legs",
        "sub_region": "glutes",
        "difficulty": "medium",
        "equipment": ["dumbbell", "barbell"],
        "targets": ["gluteus_maximus", "gluteus_medius"],
        "type": "compound",
        "nippard_tier": "S",
        "research_notes": "Nippard S-tier; lean 30° forward for max glute",
        "rest": 90
    },
    {
        "id": "machine-hip-abduction",
        "name": "Machine Hip Abduction",
        "muscle_group": "legs",
        "sub_region": "glutes",
        "difficulty": "easy",
        "equipment": ["machine"],
        "targets": ["gluteus_medius", "gluteus_minimus"],
        "type": "isolation",
        "nippard_tier": "S",
        "research_notes": "Nippard S-tier for upper glutes; lean 30° forward",
        "rest": 60
    },
    {
        "id": "step-ups",
        "name": "Step-Ups",
        "muscle_group": "legs",
        "sub_region": "glutes",
        "difficulty": "medium",
        "equipment": ["bench", "dumbbell"],
        "targets": ["gluteus_maximus", "gluteus_medius", "gluteus_minimus"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Systematic review: highest GMax activation",
        "rest": 90
    },
    {
        "id": "deep-back-squat",
        "name": "Deep Back Squat",
        "muscle_group": "legs",
        "sub_region": "glutes",
        "difficulty": "medium",
        "equipment": ["barbell", "rack"],
        "targets": ["gluteus_maximus", "gluteus_medius", "adductors"],
        "type": "compound",
        "nippard_tier": "A",
        "research_notes": "Nippard A-tier; 140° depth increases glute growth 65%",
        "rest": 180
    },
    {
        "id": "cable-kickback",
        "name": "Cable Kickback",
        "muscle_group": "legs",
        "sub_region": "glutes",
        "difficulty": "medium",
        "equipment": ["cable"],
        "targets": ["gluteus_maximus", "gluteus_medius"],
        "type": "isolation",
        "nippard_tier": "A",
        "research_notes": "Nippard A-tier; kick up and out diagonally",
        "rest": 60
    },
    {
        "id": "bulgarian-split-squat-glutes",
        "name": "Bulgarian Split Squat",
        "muscle_group": "legs",
        "sub_region": "glutes",
        "difficulty": "hard",
        "equipment": ["dumbbell", "bench"],
        "targets": ["gluteus_maximus", "gluteus_medius"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Very high GMax activation (systematic review)",
        "rest": 90
    },
    {
        "id": "machine-hip-thrust",
        "name": "Machine Hip Thrust",
        "muscle_group": "legs",
        "sub_region": "glutes",
        "difficulty": "medium",
        "equipment": ["machine"],
        "targets": ["gluteus_maximus"],
        "type": "compound",
        "nippard_tier": "A",
        "research_notes": "Nippard A-tier; minimizes setup time",
        "rest": 90
    },
    {
        "id": "single-leg-hip-thrust",
        "name": "Single-Leg Hip Thrust",
        "muscle_group": "legs",
        "sub_region": "glutes",
        "difficulty": "medium",
        "equipment": ["bench"],
        "targets": ["gluteus_maximus", "gluteus_medius", "gluteus_minimus"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Unilateral; addresses imbalances",
        "rest": 90
    },
    {
        "id": "glute-bridge",
        "name": "Glute Bridge",
        "muscle_group": "legs",
        "sub_region": "glutes",
        "difficulty": "easy",
        "equipment": ["bodyweight", "dumbbell"],
        "targets": ["gluteus_maximus"],
        "type": "compound",
        "nippard_tier": "B",
        "research_notes": "B-tier; great for beginners",
        "rest": 60
    },
    {
        "id": "cable-pull-through",
        "name": "Cable Pull-Through",
        "muscle_group": "legs",
        "sub_region": "glutes",
        "difficulty": "medium",
        "equipment": ["cable"],
        "targets": ["gluteus_maximus", "hamstrings"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Band tension increases at lockout",
        "rest": 90
    },
    {
        "id": "side-lying-hip-abduction",
        "name": "Side-Lying Hip Abduction",
        "muscle_group": "legs",
        "sub_region": "glutes",
        "difficulty": "easy",
        "equipment": ["bodyweight"],
        "targets": ["gluteus_medius", "gluteus_minimus"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "JOSPT: best gluteus medius exercise",
        "rest": 60
    },
    {
        "id": "lateral-band-walks",
        "name": "Lateral Band Walks",
        "muscle_group": "legs",
        "sub_region": "glutes",
        "difficulty": "easy",
        "equipment": ["bodyweight"],
        "targets": ["gluteus_medius", "gluteus_minimus"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "Excellent warmup; functional activation",
        "rest": 60
    },
    {
        "id": "reverse-lunge",
        "name": "Reverse Lunge",
        "muscle_group": "legs",
        "sub_region": "glutes",
        "difficulty": "medium",
        "equipment": ["dumbbell", "barbell"],
        "targets": ["gluteus_maximus", "quads", "hamstrings"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Better glute emphasis than forward lunges",
        "rest": 90
    },
]
