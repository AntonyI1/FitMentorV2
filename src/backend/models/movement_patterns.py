"""Movement pattern classification for exercise redundancy prevention.

Each exercise is mapped to a movement pattern. Exercises with the same pattern
target muscles similarly and should not both appear in the same workout to
avoid redundancy.

Movement patterns are organized by muscle group and represent distinct
biomechanical actions that provide unique stimulus.
"""

# Movement pattern definitions with descriptions
PATTERN_DESCRIPTIONS = {
    # Chest patterns
    "chest_horizontal_press": "Flat pressing (bench press variations)",
    "chest_incline_press": "Incline pressing (15-45° angle)",
    "chest_decline_press": "Decline pressing or dips with forward lean",
    "chest_fly_upper": "Fly movements targeting upper chest (low-to-high)",
    "chest_fly_mid": "Fly movements targeting mid chest (horizontal)",
    "chest_fly_lower": "Fly movements targeting lower chest (high-to-low)",

    # Back patterns
    "back_vertical_pull": "Pulldowns and pull-ups (vertical pulling)",
    "back_horizontal_row_wide": "Wide-grip rows (upper back emphasis)",
    "back_horizontal_row_close": "Close/neutral grip rows (lat emphasis)",
    "back_shrug": "Shrugging movements (upper traps)",
    "back_pullover": "Pullover and straight-arm pulldown (lat isolation)",
    "back_face_pull": "Face pulls and rear delt rows",
    "back_extension": "Spinal extension movements",
    "back_hinge": "Hip hinge with back emphasis (deadlift variations)",

    # Shoulder patterns
    "shoulder_overhead_press": "Vertical pressing movements",
    "shoulder_lateral_raise_cable": "Cable lateral raises (constant tension)",
    "shoulder_lateral_raise_dumbbell": "Dumbbell lateral raises",
    "shoulder_lateral_raise_machine": "Machine lateral raises",
    "shoulder_rear_fly_cable": "Cable rear delt flys",
    "shoulder_rear_fly_dumbbell": "Dumbbell rear delt flys",
    "shoulder_rear_fly_machine": "Machine rear delt flys (reverse pec deck)",
    "shoulder_upright_row": "Upright rowing movements",

    # Biceps patterns
    "biceps_preacher": "Preacher/spider curls (arm in front, short head)",
    "biceps_standing_curl": "Standing barbell/EZ bar curls",
    "biceps_incline_curl": "Incline curls (arm behind, long head stretch)",
    "biceps_cable_curl": "Cable curl variations",
    "biceps_hammer": "Neutral grip curls (brachialis + long head)",
    "biceps_concentration": "Concentration curls (peak contraction)",
    "biceps_chinup": "Chin-up (compound biceps)",

    # Triceps patterns
    "triceps_pushdown": "Pushdown variations (lateral/medial heads)",
    "triceps_overhead_cable": "Overhead cable extensions (long head)",
    "triceps_overhead_dumbbell": "Overhead dumbbell extensions (long head)",
    "triceps_skull_crusher": "Lying extensions/skull crushers",
    "triceps_close_grip_press": "Close-grip pressing (compound)",
    "triceps_dip": "Dip variations (compound)",
    "triceps_kickback": "Kickback variations",

    # Quad patterns
    "quad_squat_bilateral": "Bilateral squats (back squat, front squat, hack)",
    "quad_squat_unilateral": "Unilateral squats (split squat, lunge)",
    "quad_leg_press": "Leg press variations",
    "quad_leg_extension": "Leg extension (quad isolation)",
    "quad_sissy_squat": "Sissy squat / reverse nordic (rectus femoris)",

    # Hamstring patterns
    "hamstring_leg_curl_seated": "Seated leg curl (lengthened position)",
    "hamstring_leg_curl_lying": "Lying/prone leg curl",
    "hamstring_hip_hinge": "RDL and stiff-leg deadlift",
    "hamstring_glute_ham": "Glute-ham raise and nordic curl",

    # Glute patterns
    "glute_hip_thrust": "Hip thrust variations",
    "glute_bridge": "Glute bridge (lighter hip thrust)",
    "glute_squat_deep": "Deep squats for glutes",
    "glute_lunge": "Lunge variations for glutes",
    "glute_abduction_machine": "Machine hip abduction",
    "glute_abduction_floor": "Floor/bodyweight abduction",
    "glute_kickback": "Cable/bodyweight kickbacks",
    "glute_step_up": "Step-up variations",
}

# Map each exercise ID to its movement pattern
EXERCISE_TO_PATTERN = {
    # =========================================================================
    # CHEST EXERCISES
    # =========================================================================
    # Upper chest
    "incline-barbell-bench-press": "chest_incline_press",
    "incline-dumbbell-press": "chest_incline_press",
    "low-to-high-cable-fly": "chest_fly_upper",
    "incline-dumbbell-fly": "chest_fly_upper",
    "seated-cable-fly-low": "chest_fly_upper",
    "incline-smith-machine-press": "chest_incline_press",
    "reverse-grip-bench-press": "chest_horizontal_press",  # Flat bench with upper emphasis
    "landmine-press": "chest_incline_press",

    # Mid chest
    "machine-chest-press": "chest_horizontal_press",
    "flat-barbell-bench-press": "chest_horizontal_press",
    "flat-dumbbell-press": "chest_horizontal_press",
    "seated-cable-fly-mid": "chest_fly_mid",
    "pec-deck-machine": "chest_fly_mid",
    "cable-crossover-mid": "chest_fly_mid",
    "flat-dumbbell-fly": "chest_fly_mid",
    "push-ups-standard": "chest_horizontal_press",
    "deficit-push-ups": "chest_horizontal_press",

    # Lower chest
    "chest-dips": "chest_decline_press",
    "weighted-dips": "chest_decline_press",
    "decline-barbell-bench-press": "chest_decline_press",
    "decline-dumbbell-press": "chest_decline_press",
    "high-to-low-cable-fly": "chest_fly_lower",
    "decline-push-ups": "chest_decline_press",
    "decline-dumbbell-fly": "chest_fly_lower",
    "dip-machine-assisted": "chest_decline_press",

    # =========================================================================
    # ARM EXERCISES - BICEPS
    # =========================================================================
    # Biceps short head
    "preacher-curl": "biceps_preacher",
    "concentration-curl": "biceps_concentration",
    "wide-grip-barbell-curl": "biceps_standing_curl",
    "wide-grip-cable-curl": "biceps_cable_curl",
    "spider-curl": "biceps_preacher",
    "ez-bar-curl-wide": "biceps_standing_curl",
    "machine-preacher-curl": "biceps_preacher",
    "no-money-curl": "biceps_standing_curl",

    # Biceps long head
    "bayesian-cable-curl": "biceps_cable_curl",
    "incline-dumbbell-curl": "biceps_incline_curl",
    "drag-curl": "biceps_standing_curl",
    "hammer-curl": "biceps_hammer",
    "chin-up": "biceps_chinup",
    "lying-flat-bench-curl": "biceps_incline_curl",
    "narrow-grip-ez-bar-curl": "biceps_standing_curl",
    "overhead-cable-curl": "biceps_cable_curl",

    # =========================================================================
    # ARM EXERCISES - TRICEPS
    # =========================================================================
    # Triceps lateral/medial
    "cable-pushdown-rope": "triceps_pushdown",
    "cable-pushdown-straight-bar": "triceps_pushdown",
    "reverse-grip-pushdown": "triceps_pushdown",
    "close-grip-bench-press": "triceps_close_grip_press",
    "diamond-push-ups": "triceps_close_grip_press",
    "bench-dips": "triceps_dip",
    "tricep-kickback-cable": "triceps_kickback",
    "jm-press": "triceps_close_grip_press",

    # Triceps long head
    "overhead-cable-extension-straight-bar": "triceps_overhead_cable",
    "skull-crushers": "triceps_skull_crusher",
    "dumbbell-overhead-extension": "triceps_overhead_dumbbell",
    "cable-overhead-extension-rope": "triceps_overhead_cable",
    "incline-dumbbell-kickback": "triceps_kickback",
    "weighted-dips-upright": "triceps_dip",
    "katana-cable-extension": "triceps_overhead_cable",

    # =========================================================================
    # SHOULDER EXERCISES
    # =========================================================================
    # Front delt
    "machine-shoulder-press": "shoulder_overhead_press",
    "seated-dumbbell-overhead-press": "shoulder_overhead_press",
    "standing-barbell-overhead-press": "shoulder_overhead_press",
    "dumbbell-overhead-press-standing": "shoulder_overhead_press",
    "arnold-press": "shoulder_overhead_press",
    "incline-bench-press-shoulders": "chest_incline_press",  # Cross-listed
    "front-raise": "shoulder_lateral_raise_dumbbell",  # Similar pattern
    "push-up-shoulders": "chest_horizontal_press",  # Cross-listed

    # Side delt
    "single-arm-cable-lateral-raise": "shoulder_lateral_raise_cable",
    "cable-y-raise": "shoulder_lateral_raise_cable",
    "behind-back-cuffed-cable-lateral-raise": "shoulder_lateral_raise_cable",
    "cross-body-cable-lateral-raise": "shoulder_lateral_raise_cable",
    "lean-in-dumbbell-lateral-raise": "shoulder_lateral_raise_dumbbell",
    "standing-dumbbell-lateral-raise": "shoulder_lateral_raise_dumbbell",
    "arnold-style-side-lying-raise": "shoulder_lateral_raise_dumbbell",
    "atlantis-machine-lateral-raise": "shoulder_lateral_raise_machine",
    "upright-row": "shoulder_upright_row",
    "45-degree-incline-row-shoulders": "shoulder_rear_fly_dumbbell",

    # Rear delt
    "reverse-cable-crossover": "shoulder_rear_fly_cable",
    "reverse-pec-deck": "shoulder_rear_fly_machine",
    "lying-incline-rear-delt-fly": "shoulder_rear_fly_dumbbell",
    "rope-face-pull": "back_face_pull",
    "seated-rear-lateral-raise": "shoulder_rear_fly_dumbbell",
    "45-degree-incline-row-rear-delt": "shoulder_rear_fly_dumbbell",
    "bent-over-reverse-dumbbell-fly": "shoulder_rear_fly_dumbbell",
    "chest-supported-row-rear-delt": "back_horizontal_row_close",

    # =========================================================================
    # BACK EXERCISES
    # =========================================================================
    # Upper back
    "i-y-t-raises": "back_face_pull",
    "face-pulls-omni": "back_face_pull",
    "bent-over-row-wide": "back_horizontal_row_wide",
    "chest-supported-row-wide": "back_horizontal_row_wide",
    "inverted-row": "back_horizontal_row_wide",
    "seated-cable-row-wide": "back_horizontal_row_wide",
    "barbell-shrugs": "back_shrug",
    "cable-shrugs": "back_shrug",
    "cable-y-raise-traps": "back_face_pull",
    "reverse-pec-deck-back": "shoulder_rear_fly_machine",

    # Lats
    "pull-ups": "back_vertical_pull",
    "chin-ups-back": "back_vertical_pull",
    "lat-pulldown": "back_vertical_pull",
    "single-arm-lat-pulldown": "back_vertical_pull",
    "chest-supported-row-neutral": "back_horizontal_row_close",
    "seated-cable-row-close": "back_horizontal_row_close",
    "single-arm-dumbbell-row": "back_horizontal_row_close",
    "bent-over-row-underhand": "back_horizontal_row_close",
    "straight-arm-pulldown": "back_pullover",
    "dumbbell-pullover": "back_pullover",
    "kroc-row": "back_horizontal_row_close",

    # Lower back
    "conventional-deadlift": "back_hinge",
    "romanian-deadlift-back": "back_hinge",
    "45-degree-back-extension": "back_extension",
    "prone-lumbar-extension": "back_extension",
    "good-mornings-back": "back_hinge",
    "superman-hold": "back_extension",
    "bird-dog": "back_extension",
    "glute-bridge-back": "glute_bridge",
    "jefferson-curl": "back_extension",

    # =========================================================================
    # LEG EXERCISES - QUADRICEPS
    # =========================================================================
    "barbell-back-squat": "quad_squat_bilateral",
    "barbell-front-squat": "quad_squat_bilateral",
    "hack-squat": "quad_squat_bilateral",
    "pendulum-squat": "quad_squat_bilateral",
    "smith-machine-squat": "quad_squat_bilateral",
    "leg-extension": "quad_leg_extension",
    "bulgarian-split-squat": "quad_squat_unilateral",
    "45-degree-leg-press": "quad_leg_press",
    "goblet-squat": "quad_squat_bilateral",
    "reverse-nordic-curl": "quad_sissy_squat",
    "sissy-squat": "quad_sissy_squat",
    "walking-lunges-short": "quad_squat_unilateral",

    # =========================================================================
    # LEG EXERCISES - HAMSTRINGS
    # =========================================================================
    "seated-leg-curl": "hamstring_leg_curl_seated",
    "romanian-deadlift": "hamstring_hip_hinge",
    "nordic-hamstring-curl": "hamstring_glute_ham",
    "glute-ham-raise": "hamstring_glute_ham",
    "lying-leg-curl": "hamstring_leg_curl_lying",
    "stiff-leg-deadlift": "hamstring_hip_hinge",
    "single-leg-rdl": "hamstring_hip_hinge",
    "stability-ball-hamstring-curl": "hamstring_leg_curl_lying",
    "good-mornings": "hamstring_hip_hinge",

    # =========================================================================
    # LEG EXERCISES - GLUTES
    # =========================================================================
    "barbell-hip-thrust": "glute_hip_thrust",
    "walking-lunges-long": "glute_lunge",
    "machine-hip-abduction": "glute_abduction_machine",
    "step-ups": "glute_step_up",
    "deep-back-squat": "glute_squat_deep",
    "cable-kickback": "glute_kickback",
    "bulgarian-split-squat-glutes": "quad_squat_unilateral",
    "machine-hip-thrust": "glute_hip_thrust",
    "single-leg-hip-thrust": "glute_hip_thrust",
    "glute-bridge": "glute_bridge",
    "cable-pull-through": "glute_hip_thrust",
    "side-lying-hip-abduction": "glute_abduction_floor",
    "lateral-band-walks": "glute_abduction_floor",
    "reverse-lunge": "glute_lunge",
}


def get_movement_pattern(exercise_id: str) -> str | None:
    """Get the movement pattern for an exercise.

    Args:
        exercise_id: The exercise ID (slug format)

    Returns:
        Movement pattern string or None if not found
    """
    return EXERCISE_TO_PATTERN.get(exercise_id)


def get_pattern_description(pattern: str) -> str:
    """Get a human-readable description of a movement pattern."""
    return PATTERN_DESCRIPTIONS.get(pattern, "Unknown pattern")


def are_exercises_redundant(exercise_id_1: str, exercise_id_2: str) -> bool:
    """Check if two exercises share the same movement pattern.

    Args:
        exercise_id_1: First exercise ID
        exercise_id_2: Second exercise ID

    Returns:
        True if exercises are redundant (same pattern), False otherwise
    """
    pattern_1 = get_movement_pattern(exercise_id_1)
    pattern_2 = get_movement_pattern(exercise_id_2)

    if pattern_1 is None or pattern_2 is None:
        return False

    return pattern_1 == pattern_2


def get_exercises_by_pattern(pattern: str) -> list[str]:
    """Get all exercise IDs that match a movement pattern.

    Args:
        pattern: The movement pattern to search for

    Returns:
        List of exercise IDs with that pattern
    """
    return [eid for eid, p in EXERCISE_TO_PATTERN.items() if p == pattern]


def get_patterns_for_muscle_group(muscle_group: str) -> list[str]:
    """Get all movement patterns relevant to a muscle group.

    Args:
        muscle_group: One of chest, arms, shoulders, back, legs

    Returns:
        List of movement patterns for that muscle group
    """
    prefix_map = {
        "chest": ["chest_"],
        "arms": ["biceps_", "triceps_"],
        "shoulders": ["shoulder_"],
        "back": ["back_"],
        "legs": ["quad_", "hamstring_", "glute_"],
    }

    prefixes = prefix_map.get(muscle_group, [])
    patterns = set()

    for pattern in PATTERN_DESCRIPTIONS.keys():
        for prefix in prefixes:
            if pattern.startswith(prefix):
                patterns.add(pattern)
                break

    return list(patterns)
