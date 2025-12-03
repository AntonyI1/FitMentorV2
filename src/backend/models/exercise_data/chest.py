"""Chest exercises - 24 exercises across 3 sub-regions.

Sub-regions:
- upper_chest (clavicular head): 8 exercises
- mid_chest (sternal head): 10 exercises
- lower_chest (costal fibers): 8 exercises

Research note: EMG research from Rodríguez-Ridao et al. (2020) confirms that
30° incline produces maximum upper chest activation, while flat and decline
variations emphasize the mid and lower portions.
"""

CHEST_EXERCISES = [
    # =========================================================================
    # UPPER CHEST (Clavicular Head) - 8 exercises
    # =========================================================================
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
        "research_notes": "Nippard A-tier; EMG peaks at 30° incline (~30% MVIC)",
        "rest": 120
    },
    {
        "id": "incline-dumbbell-press",
        "name": "Incline Dumbbell Press",
        "muscle_group": "chest",
        "sub_region": "upper_chest",
        "difficulty": "medium",
        "equipment": ["dumbbell", "bench"],
        "targets": ["upper_pec", "anterior_deltoid", "triceps"],
        "type": "compound",
        "nippard_tier": "A",
        "research_notes": "Nippard A-tier; deeper stretch than barbell at 15-30°",
        "rest": 120
    },
    {
        "id": "low-to-high-cable-fly",
        "name": "Low-to-High Cable Fly",
        "muscle_group": "chest",
        "sub_region": "upper_chest",
        "difficulty": "easy",
        "equipment": ["cable"],
        "targets": ["upper_pec", "anterior_deltoid"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "Follows clavicular fiber direction; constant tension",
        "rest": 60
    },
    {
        "id": "incline-dumbbell-fly",
        "name": "Incline Dumbbell Fly",
        "muscle_group": "chest",
        "sub_region": "upper_chest",
        "difficulty": "easy",
        "equipment": ["dumbbell", "bench"],
        "targets": ["upper_pec"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "Isolation emphasizing stretched position",
        "rest": 60
    },
    {
        "id": "seated-cable-fly-low",
        "name": "Seated Cable Fly (Low Position)",
        "muscle_group": "chest",
        "sub_region": "upper_chest",
        "difficulty": "easy",
        "equipment": ["cable", "bench"],
        "targets": ["upper_pec"],
        "type": "isolation",
        "nippard_tier": "S",
        "research_notes": "Nippard S-tier; eliminates balance, maximizes pec tension",
        "rest": 60
    },
    {
        "id": "incline-smith-machine-press",
        "name": "Incline Smith Machine Press",
        "muscle_group": "chest",
        "sub_region": "upper_chest",
        "difficulty": "medium",
        "equipment": ["machine", "bench"],
        "targets": ["upper_pec", "anterior_deltoid", "triceps"],
        "type": "compound",
        "nippard_tier": "A",
        "research_notes": "Nippard A-tier; safe failure training",
        "rest": 120
    },
    {
        "id": "reverse-grip-bench-press",
        "name": "Reverse-Grip Bench Press",
        "muscle_group": "chest",
        "sub_region": "upper_chest",
        "difficulty": "hard",
        "equipment": ["barbell", "bench", "rack"],
        "targets": ["upper_pec", "triceps"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Supinated grip activates clavicular head on flat bench",
        "rest": 120
    },
    {
        "id": "landmine-press",
        "name": "Landmine Press",
        "muscle_group": "chest",
        "sub_region": "upper_chest",
        "difficulty": "medium",
        "equipment": ["barbell"],
        "targets": ["upper_pec", "anterior_deltoid"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Arc pattern aligns with upper chest fibers",
        "rest": 90
    },

    # =========================================================================
    # MID CHEST (Sternal Head) - 10 exercises
    # =========================================================================
    {
        "id": "machine-chest-press",
        "name": "Machine Chest Press",
        "muscle_group": "chest",
        "sub_region": "mid_chest",
        "difficulty": "easy",
        "equipment": ["machine"],
        "targets": ["mid_pec", "anterior_deltoid", "triceps"],
        "type": "compound",
        "nippard_tier": "S",
        "research_notes": "Nippard S-tier #1; deep stretch, smooth resistance, easy progression",
        "rest": 90
    },
    {
        "id": "flat-barbell-bench-press",
        "name": "Flat Barbell Bench Press",
        "muscle_group": "chest",
        "sub_region": "mid_chest",
        "difficulty": "medium",
        "equipment": ["barbell", "bench", "rack"],
        "targets": ["all_pec_regions", "triceps"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "ACE study: most effective overall chest exercise",
        "rest": 120
    },
    {
        "id": "flat-dumbbell-press",
        "name": "Flat Dumbbell Press",
        "muscle_group": "chest",
        "sub_region": "mid_chest",
        "difficulty": "medium",
        "equipment": ["dumbbell", "bench"],
        "targets": ["mid_pec", "triceps"],
        "type": "compound",
        "nippard_tier": "A",
        "research_notes": "Nippard A-tier; superior ROM vs barbell",
        "rest": 120
    },
    {
        "id": "seated-cable-fly-mid",
        "name": "Seated Cable Fly (Mid Position)",
        "muscle_group": "chest",
        "sub_region": "mid_chest",
        "difficulty": "easy",
        "equipment": ["cable", "bench"],
        "targets": ["mid_pec"],
        "type": "isolation",
        "nippard_tier": "S",
        "research_notes": "Nippard S-tier isolation; constant tension throughout",
        "rest": 60
    },
    {
        "id": "pec-deck-machine",
        "name": "Pec Deck Machine",
        "muscle_group": "chest",
        "sub_region": "mid_chest",
        "difficulty": "easy",
        "equipment": ["machine"],
        "targets": ["mid_pec"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "ACE study: 98% activation vs bench press",
        "rest": 60
    },
    {
        "id": "cable-crossover-mid",
        "name": "Cable Crossover (Mid Height)",
        "muscle_group": "chest",
        "sub_region": "mid_chest",
        "difficulty": "easy",
        "equipment": ["cable"],
        "targets": ["mid_pec"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "ACE study: 93% activation; excellent stretch",
        "rest": 60
    },
    {
        "id": "flat-dumbbell-fly",
        "name": "Flat Dumbbell Fly",
        "muscle_group": "chest",
        "sub_region": "mid_chest",
        "difficulty": "easy",
        "equipment": ["dumbbell", "bench"],
        "targets": ["mid_pec"],
        "type": "isolation",
        "nippard_tier": "A",
        "research_notes": "Nippard A-tier; emphasizes stretch",
        "rest": 60
    },
    {
        "id": "push-ups-standard",
        "name": "Push-Ups (Standard)",
        "muscle_group": "chest",
        "sub_region": "mid_chest",
        "difficulty": "easy",
        "equipment": ["bodyweight"],
        "targets": ["mid_pec", "triceps", "anterior_deltoid"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Comparable activation to bench at similar intensity",
        "rest": 60
    },
    {
        "id": "deficit-push-ups",
        "name": "Deficit Push-Ups",
        "muscle_group": "chest",
        "sub_region": "mid_chest",
        "difficulty": "medium",
        "equipment": ["bodyweight", "bench"],
        "targets": ["mid_pec", "triceps"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Hands elevated for deeper pec stretch",
        "rest": 90
    },

    # =========================================================================
    # LOWER CHEST (Costal Fibers) - 8 exercises
    # =========================================================================
    {
        "id": "chest-dips",
        "name": "Chest Dips",
        "muscle_group": "chest",
        "sub_region": "lower_chest",
        "difficulty": "medium",
        "equipment": ["bodyweight"],
        "targets": ["lower_pec", "triceps"],
        "type": "compound",
        "nippard_tier": "A",
        "research_notes": "Nippard A-tier; 30-45° forward lean maximizes lower pec",
        "rest": 120
    },
    {
        "id": "weighted-dips",
        "name": "Weighted Dips",
        "muscle_group": "chest",
        "sub_region": "lower_chest",
        "difficulty": "hard",
        "equipment": ["bodyweight"],
        "targets": ["lower_pec", "triceps"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Deep stretch induces high mechanical tension",
        "rest": 120
    },
    {
        "id": "decline-barbell-bench-press",
        "name": "Decline Barbell Bench Press",
        "muscle_group": "chest",
        "sub_region": "lower_chest",
        "difficulty": "medium",
        "equipment": ["barbell", "bench", "rack"],
        "targets": ["lower_pec", "triceps"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Higher lower sternal activation vs flat (Schoenfeld 2016)",
        "rest": 120
    },
    {
        "id": "decline-dumbbell-press",
        "name": "Decline Dumbbell Press",
        "muscle_group": "chest",
        "sub_region": "lower_chest",
        "difficulty": "medium",
        "equipment": ["dumbbell", "bench"],
        "targets": ["lower_pec", "triceps"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Greater ROM than barbell; 15-30° decline optimal",
        "rest": 120
    },
    {
        "id": "high-to-low-cable-fly",
        "name": "High-to-Low Cable Fly",
        "muscle_group": "chest",
        "sub_region": "lower_chest",
        "difficulty": "easy",
        "equipment": ["cable"],
        "targets": ["lower_pec"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "Follows lower fiber direction; constant tension",
        "rest": 60
    },
    {
        "id": "decline-push-ups",
        "name": "Decline Push-Ups",
        "muscle_group": "chest",
        "sub_region": "lower_chest",
        "difficulty": "easy",
        "equipment": ["bodyweight", "bench"],
        "targets": ["lower_pec", "triceps"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Feet elevated changes angle to bias lower chest",
        "rest": 60
    },
    {
        "id": "decline-dumbbell-fly",
        "name": "Decline Dumbbell Fly",
        "muscle_group": "chest",
        "sub_region": "lower_chest",
        "difficulty": "easy",
        "equipment": ["dumbbell", "bench"],
        "targets": ["lower_pec"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "Isolation at decline for lower sternal fibers",
        "rest": 60
    },
    {
        "id": "dip-machine-assisted",
        "name": "Dip Machine (Assisted)",
        "muscle_group": "chest",
        "sub_region": "lower_chest",
        "difficulty": "easy",
        "equipment": ["machine"],
        "targets": ["lower_pec", "triceps"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Adjustable assistance for beginners",
        "rest": 90
    },
]
