"""Back exercises - 30 exercises across 3 sub-regions.

Sub-regions:
- upper_back (traps, rhomboids): 10 exercises
- lats (latissimus dorsi): 11 exercises
- lower_back (erector spinae): 9 exercises

Research note: The back contains multiple muscle groups requiring different
movement patterns. Vertical pulling (pulldowns, pull-ups) emphasizes lat width,
while horizontal rowing builds thickness. The ACE study found bent-over rows
activated 3 of 5 back muscles maximally and ranked second for the remaining two.
"""

BACK_EXERCISES = [
    # =========================================================================
    # UPPER BACK (Traps, Rhomboids) - 10 exercises
    # =========================================================================
    {
        "id": "i-y-t-raises",
        "name": "I-Y-T Raises (Prone)",
        "muscle_group": "back",
        "sub_region": "upper_back",
        "difficulty": "medium",
        "equipment": ["dumbbell", "bench"],
        "targets": ["middle_traps", "lower_traps", "rhomboids"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "ACE study: greatest lower trap activation of all exercises",
        "rest": 60
    },
    {
        "id": "face-pulls-omni",
        "name": "Face Pulls (Omni-Direction)",
        "muscle_group": "back",
        "sub_region": "upper_back",
        "difficulty": "easy",
        "equipment": ["cable"],
        "targets": ["middle_traps", "rear_delts", "rhomboids"],
        "type": "isolation",
        "nippard_tier": "S",
        "research_notes": "Nippard S-tier; vary height each set",
        "rest": 60
    },
    {
        "id": "bent-over-row-wide",
        "name": "Bent-Over Row (Wide Grip)",
        "muscle_group": "back",
        "sub_region": "upper_back",
        "difficulty": "hard",
        "equipment": ["barbell"],
        "targets": ["middle_traps", "rhomboids", "lats"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "ACE: best overall back exercise",
        "rest": 120
    },
    {
        "id": "chest-supported-row-wide",
        "name": "Chest-Supported Row (Wide, High Pull)",
        "muscle_group": "back",
        "sub_region": "upper_back",
        "difficulty": "medium",
        "equipment": ["machine", "dumbbell", "bench"],
        "targets": ["middle_traps", "rhomboids", "rear_delts"],
        "type": "compound",
        "nippard_tier": "S+",
        "research_notes": "Nippard S+ tier #1 back exercise",
        "rest": 90
    },
    {
        "id": "inverted-row",
        "name": "Inverted Row",
        "muscle_group": "back",
        "sub_region": "upper_back",
        "difficulty": "medium",
        "equipment": ["pullup_bar", "rack"],
        "targets": ["middle_traps", "rhomboids", "lats"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Greater mid-trap EMG than pulldowns",
        "rest": 90
    },
    {
        "id": "seated-cable-row-wide",
        "name": "Seated Cable Row (Wide Grip)",
        "muscle_group": "back",
        "sub_region": "upper_back",
        "difficulty": "easy",
        "equipment": ["cable"],
        "targets": ["middle_traps", "rhomboids", "lats"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Highest mid-trap activation in EMG research",
        "rest": 90
    },
    {
        "id": "barbell-shrugs",
        "name": "Barbell Shrugs",
        "muscle_group": "back",
        "sub_region": "upper_back",
        "difficulty": "easy",
        "equipment": ["barbell", "dumbbell"],
        "targets": ["upper_trapezius"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "Classic trap builder; add scapular retraction",
        "rest": 60
    },
    {
        "id": "cable-shrugs",
        "name": "Cable Shrugs",
        "muscle_group": "back",
        "sub_region": "upper_back",
        "difficulty": "easy",
        "equipment": ["cable"],
        "targets": ["upper_trapezius", "middle_trapezius"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "Better fiber alignment per Nippard",
        "rest": 60
    },
    {
        "id": "cable-y-raise-traps",
        "name": "Cable Y-Raise",
        "muscle_group": "back",
        "sub_region": "upper_back",
        "difficulty": "medium",
        "equipment": ["cable"],
        "targets": ["lower_trapezius", "serratus"],
        "type": "isolation",
        "nippard_tier": "S",
        "research_notes": "Nippard S-tier for lower traps",
        "rest": 60
    },
    {
        "id": "reverse-pec-deck-back",
        "name": "Reverse Pec Deck",
        "muscle_group": "back",
        "sub_region": "upper_back",
        "difficulty": "easy",
        "equipment": ["machine"],
        "targets": ["rear_delts", "middle_traps"],
        "type": "isolation",
        "nippard_tier": "S",
        "research_notes": "Nippard S-tier; smooth resistance",
        "rest": 60
    },

    # =========================================================================
    # LATS (Latissimus Dorsi) - 11 exercises
    # =========================================================================
    {
        "id": "pull-ups",
        "name": "Pull-Ups (Overhand)",
        "muscle_group": "back",
        "sub_region": "lats",
        "difficulty": "hard",
        "equipment": ["pullup_bar"],
        "targets": ["upper_lats", "teres_major", "biceps"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "EMG: highest lat activation of any exercise",
        "rest": 120
    },
    {
        "id": "chin-ups-back",
        "name": "Chin-Ups (Underhand)",
        "muscle_group": "back",
        "sub_region": "lats",
        "difficulty": "hard",
        "equipment": ["pullup_bar"],
        "targets": ["lats", "lower_lats", "biceps"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Virtually identical lat activation to pull-ups",
        "rest": 120
    },
    {
        "id": "lat-pulldown",
        "name": "Lat Pulldown (Medium Grip)",
        "muscle_group": "back",
        "sub_region": "lats",
        "difficulty": "easy",
        "equipment": ["machine"],
        "targets": ["lats", "teres_major", "biceps"],
        "type": "compound",
        "nippard_tier": "S",
        "research_notes": "Nippard S-tier; smooth, excellent stretch",
        "rest": 90
    },
    {
        "id": "single-arm-lat-pulldown",
        "name": "Single-Arm Lat Pulldown (Kneeling)",
        "muscle_group": "back",
        "sub_region": "lats",
        "difficulty": "medium",
        "equipment": ["cable"],
        "targets": ["lats", "teres_major"],
        "type": "compound",
        "nippard_tier": "S",
        "research_notes": "Nippard S-tier; greater ROM, corrects imbalances",
        "rest": 90
    },
    {
        "id": "chest-supported-row-neutral",
        "name": "Chest-Supported Row (Neutral Grip)",
        "muscle_group": "back",
        "sub_region": "lats",
        "difficulty": "medium",
        "equipment": ["machine", "dumbbell", "bench"],
        "targets": ["lats", "rhomboids", "teres_major"],
        "type": "compound",
        "nippard_tier": "S+",
        "research_notes": "Nippard S+ tier; eliminates cheating",
        "rest": 90
    },
    {
        "id": "seated-cable-row-close",
        "name": "Seated Cable Row (Close Grip)",
        "muscle_group": "back",
        "sub_region": "lats",
        "difficulty": "easy",
        "equipment": ["cable"],
        "targets": ["lats", "lower_lats", "rhomboids"],
        "type": "compound",
        "nippard_tier": "S",
        "research_notes": "Nippard S-tier; protracted scapulae = higher lat activation",
        "rest": 90
    },
    {
        "id": "single-arm-dumbbell-row",
        "name": "Single-Arm Dumbbell Row",
        "muscle_group": "back",
        "sub_region": "lats",
        "difficulty": "medium",
        "equipment": ["dumbbell", "bench"],
        "targets": ["lats", "rhomboids", "rear_delts"],
        "type": "compound",
        "nippard_tier": "A",
        "research_notes": "Nippard A-tier; elbow close = more lat emphasis",
        "rest": 90
    },
    {
        "id": "bent-over-row-underhand",
        "name": "Bent-Over Row (Underhand)",
        "muscle_group": "back",
        "sub_region": "lats",
        "difficulty": "hard",
        "equipment": ["barbell"],
        "targets": ["lats", "lower_lats", "biceps"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Slightly more lat activation than overhand",
        "rest": 120
    },
    {
        "id": "straight-arm-pulldown",
        "name": "Straight-Arm Pulldown",
        "muscle_group": "back",
        "sub_region": "lats",
        "difficulty": "medium",
        "equipment": ["cable"],
        "targets": ["lats"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "Isolates lats without bicep involvement",
        "rest": 60
    },
    {
        "id": "dumbbell-pullover",
        "name": "Dumbbell Pullover (Bottom-Half)",
        "muscle_group": "back",
        "sub_region": "lats",
        "difficulty": "medium",
        "equipment": ["dumbbell", "bench"],
        "targets": ["lats"],
        "type": "isolation",
        "nippard_tier": "A",
        "research_notes": "Nippard A-tier; stay in stretched position only",
        "rest": 60
    },
    {
        "id": "kroc-row",
        "name": "Kroc Row",
        "muscle_group": "back",
        "sub_region": "lats",
        "difficulty": "hard",
        "equipment": ["dumbbell"],
        "targets": ["lats", "rhomboids", "grip"],
        "type": "compound",
        "nippard_tier": "A",
        "research_notes": "Nippard A-tier; controlled momentum",
        "rest": 90
    },

    # =========================================================================
    # LOWER BACK (Erector Spinae) - 9 exercises
    # =========================================================================
    {
        "id": "conventional-deadlift",
        "name": "Conventional Deadlift",
        "muscle_group": "back",
        "sub_region": "lower_back",
        "difficulty": "hard",
        "equipment": ["barbell"],
        "targets": ["erector_spinae", "glutes", "hamstrings"],
        "type": "compound",
        "nippard_tier": "C",
        "research_notes": "C-tier for back hypertrophy; excellent for strength",
        "rest": 180
    },
    {
        "id": "romanian-deadlift-back",
        "name": "Romanian Deadlift",
        "muscle_group": "back",
        "sub_region": "lower_back",
        "difficulty": "medium",
        "equipment": ["barbell", "dumbbell"],
        "targets": ["erector_spinae", "hamstrings", "glutes"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Constant tension on erectors through hinge",
        "rest": 120
    },
    {
        "id": "45-degree-back-extension",
        "name": "45-Degree Back Extension",
        "muscle_group": "back",
        "sub_region": "lower_back",
        "difficulty": "medium",
        "equipment": ["machine"],
        "targets": ["erector_spinae", "glutes", "hamstrings"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "77-82% MVC activation; full ROM",
        "rest": 90
    },
    {
        "id": "prone-lumbar-extension",
        "name": "Prone Lumbar Extension",
        "muscle_group": "back",
        "sub_region": "lower_back",
        "difficulty": "hard",
        "equipment": ["bench", "dumbbell"],
        "targets": ["lumbar_multifidus", "longissimus"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "PubMed: 92%+ MVIC in lower back muscles",
        "rest": 90
    },
    {
        "id": "good-mornings-back",
        "name": "Good Mornings",
        "muscle_group": "back",
        "sub_region": "lower_back",
        "difficulty": "hard",
        "equipment": ["barbell"],
        "targets": ["erector_spinae", "hamstrings", "glutes"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Excellent for endurance and strength",
        "rest": 120
    },
    {
        "id": "superman-hold",
        "name": "Superman Hold",
        "muscle_group": "back",
        "sub_region": "lower_back",
        "difficulty": "easy",
        "equipment": ["bodyweight"],
        "targets": ["erector_spinae", "glutes", "rhomboids"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "77-82% MVC; great for beginners",
        "rest": 60
    },
    {
        "id": "bird-dog",
        "name": "Bird Dog",
        "muscle_group": "back",
        "sub_region": "lower_back",
        "difficulty": "easy",
        "equipment": ["bodyweight"],
        "targets": ["erector_spinae", "multifidus", "core"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "Evidence-based rehab exercise; anti-rotation",
        "rest": 60
    },
    {
        "id": "glute-bridge-back",
        "name": "Glute Bridge",
        "muscle_group": "back",
        "sub_region": "lower_back",
        "difficulty": "easy",
        "equipment": ["bodyweight"],
        "targets": ["erector_spinae", "glutes"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "AAOS spine conditioning exercise",
        "rest": 60
    },
    {
        "id": "jefferson-curl",
        "name": "Jefferson Curl",
        "muscle_group": "back",
        "sub_region": "lower_back",
        "difficulty": "hard",
        "equipment": ["barbell"],
        "targets": ["erector_spinae"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "Advanced; builds mobility through full range",
        "rest": 90
    },
]
