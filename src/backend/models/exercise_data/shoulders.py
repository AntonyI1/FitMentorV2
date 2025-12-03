"""Shoulder exercises - 26 exercises across 3 sub-regions.

Sub-regions:
- front_delt (anterior deltoid): 8 exercises
- side_delt (medial deltoid): 10 exercises
- rear_delt (posterior deltoid): 8 exercises

Research note: 70-90% of shoulder training should focus on medial (side) delts—
they create shoulder width. Front delts receive substantial work from pressing
movements, while rear delts are often undertrained despite their importance
for shoulder health and aesthetics.
"""

SHOULDER_EXERCISES = [
    # =========================================================================
    # FRONT DELT (Anterior Deltoid) - 8 exercises
    # =========================================================================
    {
        "id": "machine-shoulder-press",
        "name": "Machine Shoulder Press",
        "muscle_group": "shoulders",
        "sub_region": "front_delt",
        "difficulty": "medium",
        "equipment": ["machine"],
        "targets": ["anterior_deltoid", "medial_deltoid", "triceps"],
        "type": "compound",
        "nippard_tier": "A+",
        "research_notes": "Nippard A+ tier #1; safe failure training, consistent tension",
        "rest": 120
    },
    {
        "id": "seated-dumbbell-overhead-press",
        "name": "Seated Dumbbell Overhead Press",
        "muscle_group": "shoulders",
        "sub_region": "front_delt",
        "difficulty": "medium",
        "equipment": ["dumbbell", "bench"],
        "targets": ["anterior_deltoid", "medial_deltoid"],
        "type": "compound",
        "nippard_tier": "A",
        "research_notes": "Nippard A-tier; go-to without machine access",
        "rest": 120
    },
    {
        "id": "standing-barbell-overhead-press",
        "name": "Standing Barbell Overhead Press",
        "muscle_group": "shoulders",
        "sub_region": "front_delt",
        "difficulty": "hard",
        "equipment": ["barbell", "rack"],
        "targets": ["anterior_deltoid", "core"],
        "type": "compound",
        "nippard_tier": "B+",
        "research_notes": "B+ tier; highest neuromuscular activity (Saeterbakken 2013)",
        "rest": 120
    },
    {
        "id": "dumbbell-overhead-press-standing",
        "name": "Dumbbell Overhead Press (Standing)",
        "muscle_group": "shoulders",
        "sub_region": "front_delt",
        "difficulty": "medium",
        "equipment": ["dumbbell"],
        "targets": ["anterior_deltoid", "medial_deltoid"],
        "type": "compound",
        "nippard_tier": "A",
        "research_notes": "Nippard A-tier; greater ROM than barbell",
        "rest": 120
    },
    {
        "id": "arnold-press",
        "name": "Arnold Press",
        "muscle_group": "shoulders",
        "sub_region": "front_delt",
        "difficulty": "medium",
        "equipment": ["dumbbell", "bench"],
        "targets": ["anterior_deltoid", "medial_deltoid"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Higher anterior AND medial activation than standard press",
        "rest": 120
    },
    {
        "id": "incline-bench-press-shoulders",
        "name": "Incline Bench Press",
        "muscle_group": "shoulders",
        "sub_region": "front_delt",
        "difficulty": "medium",
        "equipment": ["barbell", "dumbbell", "bench"],
        "targets": ["upper_pec", "anterior_deltoid"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Greatest anterior delt among horizontal pressing",
        "rest": 120
    },
    {
        "id": "front-raise",
        "name": "Front Raise (Dumbbell/Cable)",
        "muscle_group": "shoulders",
        "sub_region": "front_delt",
        "difficulty": "easy",
        "equipment": ["dumbbell", "cable"],
        "targets": ["anterior_deltoid"],
        "type": "isolation",
        "nippard_tier": "D",
        "research_notes": "D-tier per Nippard; redundant with pressing",
        "rest": 60
    },
    {
        "id": "push-up-shoulders",
        "name": "Push-Up",
        "muscle_group": "shoulders",
        "sub_region": "front_delt",
        "difficulty": "easy",
        "equipment": ["bodyweight"],
        "targets": ["anterior_deltoid"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Trains front delts as secondary mover",
        "rest": 60
    },

    # =========================================================================
    # SIDE DELT (Medial Deltoid) - 10 exercises
    # =========================================================================
    {
        "id": "single-arm-cable-lateral-raise",
        "name": "Single-Arm Cable Lateral Raise",
        "muscle_group": "shoulders",
        "sub_region": "side_delt",
        "difficulty": "easy",
        "equipment": ["cable"],
        "targets": ["lateral_deltoid"],
        "type": "isolation",
        "nippard_tier": "S+",
        "research_notes": "Nippard S+ tier #1; maximum tension in stretched position",
        "rest": 60
    },
    {
        "id": "cable-y-raise",
        "name": "Cable Y-Raise",
        "muscle_group": "shoulders",
        "sub_region": "side_delt",
        "difficulty": "medium",
        "equipment": ["cable"],
        "targets": ["lateral_deltoid"],
        "type": "isolation",
        "nippard_tier": "S",
        "research_notes": "Nippard S-tier; both arms, time-efficient",
        "rest": 60
    },
    {
        "id": "behind-back-cuffed-cable-lateral-raise",
        "name": "Behind-Back Cuffed Cable Lateral Raise",
        "muscle_group": "shoulders",
        "sub_region": "side_delt",
        "difficulty": "medium",
        "equipment": ["cable"],
        "targets": ["lateral_deltoid"],
        "type": "isolation",
        "nippard_tier": "S",
        "research_notes": "Nippard S-tier; tremendous stretch across body",
        "rest": 60
    },
    {
        "id": "cross-body-cable-lateral-raise",
        "name": "Cross-Body Cable Lateral Raise",
        "muscle_group": "shoulders",
        "sub_region": "side_delt",
        "difficulty": "medium",
        "equipment": ["cable"],
        "targets": ["lateral_deltoid"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "Extended ROM for medial delt development",
        "rest": 60
    },
    {
        "id": "lean-in-dumbbell-lateral-raise",
        "name": "Lean-In Dumbbell Lateral Raise",
        "muscle_group": "shoulders",
        "sub_region": "side_delt",
        "difficulty": "medium",
        "equipment": ["dumbbell", "bench"],
        "targets": ["lateral_deltoid"],
        "type": "isolation",
        "nippard_tier": "A",
        "research_notes": "Nippard A-tier; tension when stretched",
        "rest": 60
    },
    {
        "id": "standing-dumbbell-lateral-raise",
        "name": "Standing Dumbbell Lateral Raise",
        "muscle_group": "shoulders",
        "sub_region": "side_delt",
        "difficulty": "easy",
        "equipment": ["dumbbell"],
        "targets": ["lateral_deltoid"],
        "type": "isolation",
        "nippard_tier": "B",
        "research_notes": "B-tier; zero tension at bottom but time-efficient",
        "rest": 60
    },
    {
        "id": "arnold-style-side-lying-raise",
        "name": "Arnold-Style Side-Lying Raise",
        "muscle_group": "shoulders",
        "sub_region": "side_delt",
        "difficulty": "medium",
        "equipment": ["dumbbell", "bench"],
        "targets": ["lateral_deltoid"],
        "type": "isolation",
        "nippard_tier": "A",
        "research_notes": "Nippard A-tier; good stability and ROM",
        "rest": 60
    },
    {
        "id": "atlantis-machine-lateral-raise",
        "name": "Atlantis Standing Machine Lateral Raise",
        "muscle_group": "shoulders",
        "sub_region": "side_delt",
        "difficulty": "easy",
        "equipment": ["machine"],
        "targets": ["lateral_deltoid"],
        "type": "isolation",
        "nippard_tier": "A+",
        "research_notes": "Nippard A+ tier; smooth, consistent tension",
        "rest": 60
    },
    {
        "id": "upright-row",
        "name": "Upright Row (Cable/Rope)",
        "muscle_group": "shoulders",
        "sub_region": "side_delt",
        "difficulty": "medium",
        "equipment": ["cable", "barbell"],
        "targets": ["lateral_deltoid", "upper_traps"],
        "type": "compound",
        "nippard_tier": "B",
        "research_notes": "B-tier; ACE ranked lowest but still effective",
        "rest": 90
    },
    {
        "id": "45-degree-incline-row-shoulders",
        "name": "45-Degree Incline Row",
        "muscle_group": "shoulders",
        "sub_region": "side_delt",
        "difficulty": "medium",
        "equipment": ["dumbbell", "bench"],
        "targets": ["medial_deltoid", "posterior_deltoid"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "ACE study: highest medial delt activation",
        "rest": 90
    },

    # =========================================================================
    # REAR DELT (Posterior Deltoid) - 8 exercises
    # =========================================================================
    {
        "id": "reverse-cable-crossover",
        "name": "Reverse Cable Crossover",
        "muscle_group": "shoulders",
        "sub_region": "rear_delt",
        "difficulty": "medium",
        "equipment": ["cable"],
        "targets": ["posterior_deltoid"],
        "type": "isolation",
        "nippard_tier": "S",
        "research_notes": "Nippard S-tier #1; full ROM, constant tension",
        "rest": 60
    },
    {
        "id": "reverse-pec-deck",
        "name": "Reverse Pec Deck",
        "muscle_group": "shoulders",
        "sub_region": "rear_delt",
        "difficulty": "easy",
        "equipment": ["machine"],
        "targets": ["posterior_deltoid"],
        "type": "isolation",
        "nippard_tier": "S",
        "research_notes": "Nippard S-tier; sit sideways for deeper stretch",
        "rest": 60
    },
    {
        "id": "lying-incline-rear-delt-fly",
        "name": "Lying Incline Rear Delt Fly",
        "muscle_group": "shoulders",
        "sub_region": "rear_delt",
        "difficulty": "medium",
        "equipment": ["dumbbell", "bench"],
        "targets": ["posterior_deltoid"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "Nippard's personal favorite; bigger stretch face-down",
        "rest": 60
    },
    {
        "id": "rope-face-pull",
        "name": "Rope Face Pull (Underhand)",
        "muscle_group": "shoulders",
        "sub_region": "rear_delt",
        "difficulty": "medium",
        "equipment": ["cable"],
        "targets": ["posterior_deltoid", "external_rotators"],
        "type": "isolation",
        "nippard_tier": "A",
        "research_notes": "Nippard A-tier; set rope lower, externally rotate",
        "rest": 60
    },
    {
        "id": "seated-rear-lateral-raise",
        "name": "Seated Rear Lateral Raise",
        "muscle_group": "shoulders",
        "sub_region": "rear_delt",
        "difficulty": "medium",
        "equipment": ["dumbbell", "bench"],
        "targets": ["posterior_deltoid"],
        "type": "isolation",
        "nippard_tier": None,
        "research_notes": "ACE study: tied for highest rear delt activation",
        "rest": 60
    },
    {
        "id": "45-degree-incline-row-rear-delt",
        "name": "45-Degree Incline Row",
        "muscle_group": "shoulders",
        "sub_region": "rear_delt",
        "difficulty": "medium",
        "equipment": ["dumbbell", "bench"],
        "targets": ["posterior_deltoid", "medial_deltoid"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Excellent multi-purpose; highest activation two categories",
        "rest": 90
    },
    {
        "id": "bent-over-reverse-dumbbell-fly",
        "name": "Bent-Over Reverse Dumbbell Fly",
        "muscle_group": "shoulders",
        "sub_region": "rear_delt",
        "difficulty": "medium",
        "equipment": ["dumbbell"],
        "targets": ["posterior_deltoid"],
        "type": "isolation",
        "nippard_tier": "B",
        "research_notes": "B-tier; neutral grip increases activation",
        "rest": 60
    },
    {
        "id": "chest-supported-row-rear-delt",
        "name": "Chest-Supported Row",
        "muscle_group": "shoulders",
        "sub_region": "rear_delt",
        "difficulty": "medium",
        "equipment": ["dumbbell", "bench"],
        "targets": ["rear_deltoid", "lats"],
        "type": "compound",
        "nippard_tier": None,
        "research_notes": "Pull-up variations show greatest compound activation",
        "rest": 90
    },
]
