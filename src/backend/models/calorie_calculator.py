"""Calorie and macronutrient calculator using Mifflin-St Jeor equation."""

ACTIVITY_MULTIPLIERS = {
    "sedentary": 1.2,
    "light": 1.375,
    "moderate": 1.55,
    "active": 1.725,
    "very_active": 1.9,
}

GOAL_ADJUSTMENTS = {
    "lose": -500,
    "maintain": 0,
    "gain": 300,
}

VALID_GENDERS = {"male", "female"}
VALID_ACTIVITY_LEVELS = set(ACTIVITY_MULTIPLIERS.keys())
VALID_GOALS = set(GOAL_ADJUSTMENTS.keys())


class ValidationError(Exception):
    """Raised when input validation fails."""
    pass


def validate_input(data):
    """Validate calculator input data."""
    required = ["age", "height", "weight", "gender", "activity_level", "goal"]
    for field in required:
        if field not in data:
            raise ValidationError(f"Missing required field: {field}")

    age = data["age"]
    if not isinstance(age, int) or age < 18 or age > 80:
        raise ValidationError("age must be an integer between 18 and 80")

    height = data["height"]
    if not isinstance(height, (int, float)) or height < 140 or height > 220:
        raise ValidationError("height must be between 140 and 220 cm")

    weight = data["weight"]
    if not isinstance(weight, (int, float)) or weight < 40 or weight > 230:
        raise ValidationError("weight must be between 40 and 230 kg")

    if data["gender"] not in VALID_GENDERS:
        raise ValidationError(f"gender must be one of: {', '.join(VALID_GENDERS)}")

    if data["activity_level"] not in VALID_ACTIVITY_LEVELS:
        raise ValidationError(f"activity_level must be one of: {', '.join(VALID_ACTIVITY_LEVELS)}")

    if data["goal"] not in VALID_GOALS:
        raise ValidationError(f"goal must be one of: {', '.join(VALID_GOALS)}")


def calculate_bmr(weight, height, age, gender):
    """Calculate Basal Metabolic Rate using Mifflin-St Jeor equation."""
    base = 10 * weight + 6.25 * height - 5 * age
    if gender == "male":
        return round(base + 5)
    return round(base - 161)


def calculate_tdee(bmr, activity_level):
    """Calculate Total Daily Energy Expenditure."""
    multiplier = ACTIVITY_MULTIPLIERS[activity_level]
    return round(bmr * multiplier)


def calculate_target_calories(tdee, goal):
    """Apply goal adjustment to TDEE."""
    adjustment = GOAL_ADJUSTMENTS[goal]
    return tdee + adjustment


def calculate_ideal_body_weight(height_cm, gender):
    """Calculate ideal body weight using Devine formula.

    Returns ideal body weight in kg.
    """
    height_inches = height_cm / 2.54
    inches_over_5ft = max(0, height_inches - 60)

    if gender == "male":
        ibw_kg = 50 + 2.3 * inches_over_5ft
    else:
        ibw_kg = 45.5 + 2.3 * inches_over_5ft

    return ibw_kg


def calculate_adjusted_body_weight(weight_kg, height_cm, gender):
    """Calculate adjusted body weight for protein calculations.

    For individuals over 113kg (250 lbs), uses adjusted body weight formula:
    Adjusted BW = IBW + 0.25 × (Current weight - IBW)

    This prevents unrealistically high protein recommendations for heavier individuals.
    """
    threshold_kg = 113  # ~250 lbs

    if weight_kg <= threshold_kg:
        return weight_kg

    ibw = calculate_ideal_body_weight(height_cm, gender)
    adjusted = ibw + 0.25 * (weight_kg - ibw)
    return adjusted


def calculate_protein_grams(weight_kg, height_cm, gender, goal):
    """Calculate protein intake based on goal and body weight.

    Protein recommendations:
    - Maintenance: 1.0 g/lb (2.2 g/kg)
    - Bulking/Gain: 0.9 g/lb (2.0 g/kg)
    - Cutting/Lose: 1.2 g/lb (2.6 g/kg) - higher protein preserves muscle during deficit

    For individuals over 250 lbs, uses adjusted body weight to prevent
    unrealistically high protein targets.
    """
    adjusted_weight_kg = calculate_adjusted_body_weight(weight_kg, height_cm, gender)

    if goal == "lose":
        # Higher protein during cutting: 2.6 g/kg (~1.2 g/lb)
        protein_grams = adjusted_weight_kg * 2.6
    elif goal == "gain":
        # Bulking: 2.0 g/kg (~0.9 g/lb)
        protein_grams = adjusted_weight_kg * 2.0
    else:
        # Maintenance: 2.2 g/kg (~1.0 g/lb)
        protein_grams = adjusted_weight_kg * 2.2

    return round(protein_grams)


def calculate_macros(target_calories, weight_kg, height_cm, gender, goal):
    """Calculate macronutrient breakdown based on goal.

    Protein is calculated using evidence-based recommendations that vary by goal.
    Fat is set at 25% of calories, carbs fill the remainder.
    """
    protein_grams = calculate_protein_grams(weight_kg, height_cm, gender, goal)
    protein_calories = protein_grams * 4

    fat_calories = round(target_calories * 0.25)
    fat_grams = round(fat_calories / 9)

    carb_calories = target_calories - protein_calories - fat_calories
    carb_grams = max(0, round(carb_calories / 4))

    total = protein_calories + max(0, carb_calories) + fat_calories

    return {
        "protein": {
            "grams": protein_grams,
            "calories": protein_calories,
            "percentage": round(protein_calories / total * 100) if total > 0 else 0,
        },
        "carbs": {
            "grams": carb_grams,
            "calories": max(0, carb_calories),
            "percentage": round(max(0, carb_calories) / total * 100) if total > 0 else 0,
        },
        "fats": {
            "grams": fat_grams,
            "calories": fat_calories,
            "percentage": round(fat_calories / total * 100) if total > 0 else 0,
        },
    }


def get_recommendations(goal, gender):
    """Generate goal-specific recommendations."""
    recs = []

    if goal == "lose":
        recs.append("Aim for 0.5-1 lb weight loss per week for sustainable results")
        recs.append("Prioritize protein to preserve muscle mass during a deficit")
        recs.append("Include resistance training 3-4x per week")
    elif goal == "gain":
        recs.append("Aim for 0.25-0.5 lb weight gain per week to minimize fat gain")
        recs.append("Focus on progressive overload in your training")
        recs.append("Distribute protein intake across 4-5 meals throughout the day")
    else:
        recs.append("Monitor weight weekly and adjust calories if trending up or down")
        recs.append("Focus on food quality and nutrient timing around workouts")

    recs.append("Stay hydrated - aim for at least 8 glasses of water daily")
    recs.append("Get 7-9 hours of quality sleep for optimal recovery")

    return recs


def calculate(data):
    """Main calculation function. Returns full results dict."""
    validate_input(data)

    bmr = calculate_bmr(data["weight"], data["height"], data["age"], data["gender"])
    tdee = calculate_tdee(bmr, data["activity_level"])
    target = calculate_target_calories(tdee, data["goal"])
    macros = calculate_macros(
        target, data["weight"], data["height"], data["gender"], data["goal"]
    )
    recommendations = get_recommendations(data["goal"], data["gender"])

    return {
        "bmr": bmr,
        "tdee": tdee,
        "target_calories": target,
        "macros": macros,
        "recommendations": recommendations,
    }
