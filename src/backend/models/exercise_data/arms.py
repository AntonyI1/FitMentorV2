"""Arm exercises - 31 exercises across 4 sub-regions.

Sub-regions:
- biceps_short_head: 8 exercises (inner width, arms in front)
- biceps_long_head: 8 exercises (outer peak, arms behind body)
- triceps_lateral_medial: 8 exercises (lateral and medial heads)
- triceps_long_head: 7 exercises (largest head, ~50% of triceps mass)

Research note: The triceps long head uniquely crosses the shoulder,
requiring overhead movements for full development.
"""

ARM_EXERCISES = [
    # =========================================================================
    # BICEPS: SHORT HEAD - 8 exercises
    # =========================================================================
    {
        "id": "preacher-curl",
        "name": "Preacher Curl (45°)",
        "muscle_group": "arms",
        "sub_region": "biceps_short_head",
        "difficulty": "medium",
        "equipment": ["barbell", "bench"],
        "targets": ["biceps_short_head"],
        "type": "isolation",
        "nippard_tier": "S",
        "research_notes": "Nippard S-tier; 2023 study shows better distal bicep growth",
        "rest": 60
    },
    {
        "id": "concentration-curl",
        "name": "Concentration Curl",
        "muscle_group": "arms",
        "sub_region": "biceps_short_head",
        "difficulty": "easy",
        "equipment": ["dumbbell", "bench"],
        "targets": ["biceps_short_head", "overall_biceps"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "ACE #1 for biceps activation; minimizes cheating",
        "rest": 60
    },
    {
        "id": "wide-grip-barbell-curl",
        "name": "Wide-Grip Barbell Curl",
        "muscle_group": "arms",
        "sub_region": "biceps_short_head",
        "difficulty": "easy",
        "equipment": ["barbell"],
        "targets": ["biceps_short_head"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "Wide grip reduces long head involvement",
        "rest": 60
    },
    {
        "id": "wide-grip-cable-curl",
        "name": "Wide-Grip Cable Curl",
        "muscle_group": "arms",
        "sub_region": "biceps_short_head",
        "difficulty": "easy",
        "equipment": ["cable"],
        "targets": ["biceps_short_head"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "Constant tension throughout ROM",
        "rest": 60
    },
    {
        "id": "spider-curl",
        "name": "Spider Curl",
        "muscle_group": "arms",
        "sub_region": "biceps_short_head",
        "difficulty": "medium",
        "equipment": ["dumbbell", "bench"],
        "targets": ["biceps_short_head"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "Chest-supported; prevents momentum",
        "rest": 60
    },
    {
        "id": "ez-bar-curl-wide",
        "name": "EZ Bar Curl (Wide Grip)",
        "muscle_group": "arms",
        "sub_region": "biceps_short_head",
        "difficulty": "easy",
        "equipment": ["barbell_ez"],
        "targets": ["biceps_short_head"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "Marcolin 2018: higher activation than DB curls",
        "rest": 60
    },
    {
        "id": "machine-preacher-curl",
        "name": "Machine Preacher Curl",
        "muscle_group": "arms",
        "sub_region": "biceps_short_head",
        "difficulty": "easy",
        "equipment": ["machine"],
        "targets": ["biceps_short_head"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "Easy on joints; perfect isolation for beginners",
        "rest": 60
    },
    {
        "id": "no-money-curl",
        "name": "No Money Curl",
        "muscle_group": "arms",
        "sub_region": "biceps_short_head",
        "difficulty": "medium",
        "equipment": ["dumbbell"],
        "targets": ["biceps_short_head"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "External rotation targets inner bicep",
        "rest": 60
    },

    # =========================================================================
    # BICEPS: LONG HEAD - 8 exercises
    # =========================================================================
    {
        "id": "bayesian-cable-curl",
        "name": "Bayesian Cable Curl (Face Away)",
        "muscle_group": "arms",
        "sub_region": "biceps_long_head",
        "difficulty": "medium",
        "equipment": ["cable"],
        "targets": ["biceps_long_head"],
        "type": "isolation",
        "nippard_tier": "S",
        "research_notes": "Nippard S-tier #1; arms behind body, maximum stretch",
        "rest": 60
    },
    {
        "id": "incline-dumbbell-curl",
        "name": "Incline Dumbbell Curl",
        "muscle_group": "arms",
        "sub_region": "biceps_long_head",
        "difficulty": "medium",
        "equipment": ["dumbbell", "bench"],
        "targets": ["biceps_long_head"],
        "type": "isolation",
        "nippard_tier": "A",
        "research_notes": "Nippard A-tier; shoulder hyperextension stretches long head",
        "rest": 60
    },
    {
        "id": "drag-curl",
        "name": "Drag Curl",
        "muscle_group": "arms",
        "sub_region": "biceps_long_head",
        "difficulty": "medium",
        "equipment": ["barbell", "dumbbell"],
        "targets": ["biceps_long_head"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "Elbows pull back behind body during curl",
        "rest": 60
    },
    {
        "id": "hammer-curl",
        "name": "Hammer Curl",
        "muscle_group": "arms",
        "sub_region": "biceps_long_head",
        "difficulty": "easy",
        "equipment": ["dumbbell"],
        "targets": ["biceps_long_head", "brachialis"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "Best for biceps 'peak'; neutral grip",
        "rest": 60
    },
    {
        "id": "chin-up",
        "name": "Chin-Up",
        "muscle_group": "arms",
        "sub_region": "biceps_long_head",
        "difficulty": "hard",
        "equipment": ["pullup_bar"],
        "targets": ["biceps_long_head", "lats"],
        "type": "compound",
        "nippard_tier": "B",
        "research_notes": "Nippard B-tier; compound back/biceps",
        "rest": 120
    },
    {
        "id": "lying-flat-bench-curl",
        "name": "Lying Flat Bench Curl",
        "muscle_group": "arms",
        "sub_region": "biceps_long_head",
        "difficulty": "medium",
        "equipment": ["dumbbell", "bench"],
        "targets": ["biceps_long_head"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "Better bottom tension than incline per Nippard",
        "rest": 60
    },
    {
        "id": "narrow-grip-ez-bar-curl",
        "name": "Narrow-Grip EZ Bar Curl",
        "muscle_group": "arms",
        "sub_region": "biceps_long_head",
        "difficulty": "easy",
        "equipment": ["barbell_ez"],
        "targets": ["biceps_long_head"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "Keep elbows from moving forward",
        "rest": 60
    },
    {
        "id": "overhead-cable-curl",
        "name": "Overhead Cable Curl",
        "muscle_group": "arms",
        "sub_region": "biceps_long_head",
        "difficulty": "medium",
        "equipment": ["cable"],
        "targets": ["biceps_long_head", "biceps_peak"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "More effective long head bias than conventional curls",
        "rest": 60
    },

    # =========================================================================
    # TRICEPS: LATERAL AND MEDIAL HEADS - 8 exercises
    # =========================================================================
    {
        "id": "cable-pushdown-rope",
        "name": "Cable Pushdown (Rope)",
        "muscle_group": "arms",
        "sub_region": "triceps_lateral_medial",
        "difficulty": "easy",
        "equipment": ["cable"],
        "targets": ["triceps_lateral", "triceps_medial"],
        "type": "isolation",
        "nippard_tier": "A",
        "research_notes": "Nippard A-tier; spread rope at bottom for peak contraction",
        "rest": 60
    },
    {
        "id": "cable-pushdown-straight-bar",
        "name": "Cable Pushdown (Straight Bar)",
        "muscle_group": "arms",
        "sub_region": "triceps_lateral_medial",
        "difficulty": "easy",
        "equipment": ["cable"],
        "targets": ["triceps_lateral", "triceps_medial"],
        "type": "isolation",
        "nippard_tier": "S",
        "research_notes": "Close to S-tier; locked-in feel, easy progression",
        "rest": 60
    },
    {
        "id": "reverse-grip-pushdown",
        "name": "Reverse-Grip Pushdown",
        "muscle_group": "arms",
        "sub_region": "triceps_lateral_medial",
        "difficulty": "medium",
        "equipment": ["cable"],
        "targets": ["triceps_medial"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "Underhand grip specifically targets medial head",
        "rest": 60
    },
    {
        "id": "close-grip-bench-press",
        "name": "Close-Grip Bench Press",
        "muscle_group": "arms",
        "sub_region": "triceps_lateral_medial",
        "difficulty": "medium",
        "equipment": ["barbell", "bench"],
        "targets": ["triceps_all", "triceps_lateral"],
        "type": "compound",
        "nippard_tier": "A",
        "research_notes": "Nippard A-tier; compound for raw strength",
        "rest": 120
    },
    {
        "id": "diamond-push-ups",
        "name": "Diamond Push-Ups",
        "muscle_group": "arms",
        "sub_region": "triceps_lateral_medial",
        "difficulty": "medium",
        "equipment": ["bodyweight"],
        "targets": ["triceps_lateral", "triceps_medial"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Bohler 2011: #1 for triceps EMG activation",
        "rest": 90
    },
    {
        "id": "bench-dips",
        "name": "Bench Dips",
        "muscle_group": "arms",
        "sub_region": "triceps_lateral_medial",
        "difficulty": "easy",
        "equipment": ["bench"],
        "targets": ["triceps_lateral"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Good for beginners; compound movement",
        "rest": 90
    },
    {
        "id": "tricep-kickback-cable",
        "name": "Tricep Kickback (Cable)",
        "muscle_group": "arms",
        "sub_region": "triceps_lateral_medial",
        "difficulty": "medium",
        "equipment": ["cable"],
        "targets": ["triceps_lateral", "triceps_long_head"],
        "type": "isolation",
        "nippard_tier": "A",
        "research_notes": "Nippard A-tier; constant cable tension",
        "rest": 60
    },
    {
        "id": "jm-press",
        "name": "JM Press",
        "muscle_group": "arms",
        "sub_region": "triceps_lateral_medial",
        "difficulty": "hard",
        "equipment": ["barbell", "bench"],
        "targets": ["triceps_lateral", "triceps_all"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Hybrid movement; strength carryover",
        "rest": 120
    },

    # =========================================================================
    # TRICEPS: LONG HEAD - 7 exercises
    # =========================================================================
    {
        "id": "overhead-cable-extension-straight-bar",
        "name": "Overhead Cable Extension (Straight Bar)",
        "muscle_group": "arms",
        "sub_region": "triceps_long_head",
        "difficulty": "medium",
        "equipment": ["cable"],
        "targets": ["triceps_long_head"],
        "type": "isolation",
        "nippard_tier": "S",
        "research_notes": "Nippard S-tier #1; 2023 study: 40% more growth than pushdowns",
        "rest": 60
    },
    {
        "id": "skull-crushers",
        "name": "Skull Crushers (EZ Bar)",
        "muscle_group": "arms",
        "sub_region": "triceps_long_head",
        "difficulty": "medium",
        "equipment": ["barbell_ez", "bench"],
        "targets": ["triceps_long_head", "triceps_all"],
        "type": "isolation",
        "nippard_tier": "S",
        "research_notes": "Nippard S-tier; arc behind head for max stretch",
        "rest": 90
    },
    {
        "id": "dumbbell-overhead-extension",
        "name": "Dumbbell Overhead Extension",
        "muscle_group": "arms",
        "sub_region": "triceps_long_head",
        "difficulty": "easy",
        "equipment": ["dumbbell"],
        "targets": ["triceps_long_head"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "Overhead position maximally stretches long head",
        "rest": 60
    },
    {
        "id": "cable-overhead-extension-rope",
        "name": "Cable Overhead Extension (Rope)",
        "muscle_group": "arms",
        "sub_region": "triceps_long_head",
        "difficulty": "medium",
        "equipment": ["cable"],
        "targets": ["triceps_long_head"],
        "type": "isolation",
        "nippard_tier": "A",
        "research_notes": "Nippard A-tier; pull apart at end for contraction",
        "rest": 60
    },
    {
        "id": "incline-dumbbell-kickback",
        "name": "Incline Dumbbell Kickback",
        "muscle_group": "arms",
        "sub_region": "triceps_long_head",
        "difficulty": "medium",
        "equipment": ["dumbbell", "bench"],
        "targets": ["triceps_long_head"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "Boehren study: highest long head EMG of 9 exercises",
        "rest": 60
    },
    {
        "id": "weighted-dips-upright",
        "name": "Weighted Dips (Upright)",
        "muscle_group": "arms",
        "sub_region": "triceps_long_head",
        "difficulty": "hard",
        "equipment": ["bodyweight"],
        "targets": ["triceps_long_head", "triceps_all"],
        "type": "compound",
        "nippard_tier": "A",
        "research_notes": "Nippard A-tier; upright torso emphasizes triceps",
        "rest": 120
    },
    {
        "id": "katana-cable-extension",
        "name": "Katana Cable Extension",
        "muscle_group": "arms",
        "sub_region": "triceps_long_head",
        "difficulty": "medium",
        "equipment": ["cable"],
        "targets": ["triceps_long_head"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "Arms 30-40° forward in scapular plane",
        "rest": 60
    },
]
