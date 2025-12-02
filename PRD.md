# FitMentor - Product Requirements Document

## Overview

**FitMentor** is a fitness coaching web application that provides personalized calorie calculations and workout plan generation using evidence-based formulas and training principles from exercise science.

**Version:** 2.0.0  
**Status:** Rebuild

---

## Features

### 1. Calorie Calculator

Calculates daily calorie targets and macronutrient breakdown using the Mifflin-St Jeor equation.

**Inputs:**

| Field | Type | Constraints |
|-------|------|-------------|
| age | integer | 18-80 |
| gender | enum | male, female |
| height | float | 140-220 cm |
| weight | float | 40-200 kg |
| activity_level | enum | sedentary, light, moderate, active, very_active |
| goal | enum | lose, maintain, gain |

**Outputs:**
- BMR (Basal Metabolic Rate)
- TDEE (Total Daily Energy Expenditure)
- Target calories (adjusted for goal)
- Macronutrients (protein, carbs, fats in grams and percentages)
- Goal-specific recommendations

**Unit Support:** Metric (kg/cm) and Imperial (lbs/ft-in) with conversion.

### 2. Workout Planner

Generates multi-day workout plans based on user parameters and proven training splits.

**Inputs:**

| Field | Type | Constraints |
|-------|------|-------------|
| gender | enum | male, female |
| goal | enum | strength, hypertrophy, endurance, weight_loss |
| experience | enum | beginner, intermediate, advanced |
| equipment | array | barbell, dumbbell, machine, cable, bench, rack, pullup_bar, bodyweight |
| days_per_week | integer | 3-6 |
| session_duration | integer | 30-120 minutes (default: 60) |

**Outputs:**
- Training split (day-by-day muscle group organization)
- Exercise selection with sets, reps, rest periods
- Progression strategy
- Goal-specific training parameters

### 3. Exercise Database

38 exercises across 7 muscle groups with metadata:
- Name, muscle group, subcategory
- Equipment requirements
- Difficulty level
- Exercise type (compound/isolation)
- Rest period recommendations

---

## Tech Stack

### Backend

| Technology | Purpose |
|------------|---------|
| Python 3.8+ | Core language |
| Flask 3.0.0 | Web framework |
| flask-cors 4.0.0 | CORS handling |

### Frontend

| Technology | Purpose |
|------------|---------|
| HTML5 | Structure |
| CSS3 | Styling with CSS variables |
| Vanilla JavaScript | Interactivity |

### Data Storage

| Technology | Purpose |
|------------|---------|
| JSON Lines (.jsonl) | File-based data persistence |

---

## Architecture

### Project Structure

```
FitMentor/
├── backend/
│   ├── app.py                      # Flask API server
│   ├── models/
│   │   ├── calorie_calculator.py   # Calorie/macro calculation
│   │   ├── workout_suggester.py    # Workout plan generation
│   │   └── data_collector.py       # Data persistence
│   └── data/
│       ├── calorie_calculations.jsonl
│       └── workout_plans.jsonl
├── frontend/
│   ├── index.html
│   ├── js/
│   │   └── app.js
│   ├── css/
│   │   └── styles.css
│   └── images/
│       └── exercises/
├── requirements.txt
└── README.md
```

### System Flow

```
┌─────────────┐     HTTP/JSON      ┌─────────────┐
│   Browser   │ ◄────────────────► │  Flask API  │
│  (Frontend) │                    │  (Backend)  │
└─────────────┘                    └──────┬──────┘
                                          │
                    ┌─────────────────────┼─────────────────────┐
                    │                     │                     │
              ┌─────▼─────┐        ┌──────▼──────┐       ┌─────▼─────┐
              │  Calorie  │        │   Workout   │       │   Data    │
              │Calculator │        │  Suggester  │       │ Collector │
              └───────────┘        └─────────────┘       └───────────┘
```

---

## API Endpoints

**Base URL:** `http://localhost:5000`

### GET /
Returns API info and version.

### POST /api/calculate-calories

**Request:**
```json
{
  "age": 30,
  "height": 175,
  "weight": 80,
  "gender": "male",
  "activity_level": "moderate",
  "goal": "lose"
}
```

**Response:**
```json
{
  "bmr": 1780,
  "tdee": 2759,
  "target_calories": 2259,
  "macros": {
    "protein": { "grams": 176, "calories": 704, "percentage": 31 },
    "carbs": { "grams": 226, "calories": 904, "percentage": 40 },
    "fats": { "grams": 62, "calories": 558, "percentage": 24 }
  },
  "recommendations": ["..."]
}
```

### POST /api/suggest-workout

**Request:**
```json
{
  "gender": "male",
  "goal": "hypertrophy",
  "experience": "intermediate",
  "equipment": ["barbell", "dumbbell", "cable", "bench", "rack"],
  "days_per_week": 4,
  "session_duration": 60
}
```

**Response:**
```json
{
  "split": {
    "name": "Upper/Lower 4x/week",
    "days": [
      { "name": "Upper A", "muscle_groups": ["chest", "back", "shoulders", "biceps", "triceps"] },
      { "name": "Lower A", "muscle_groups": ["legs", "core"] }
    ]
  },
  "workouts": [{
    "day": "Upper A",
    "exercises": [{
      "name": "Barbell Bench Press",
      "sets": 3,
      "reps": "8-12",
      "rest_seconds": 120
    }]
  }],
  "progression": {
    "method": "Double Progression",
    "increment": "Increase reps to 12, then add weight",
    "deload": "20% every 5-6 weeks"
  }
}
```

### GET /api/exercises
Returns complete exercise database.

### GET /api/stats
Returns data collection statistics.

---

## Business Logic

### Calorie Calculation

**Mifflin-St Jeor Equation:**
```
Male:   BMR = 10 × weight(kg) + 6.25 × height(cm) - 5 × age + 5
Female: BMR = 10 × weight(kg) + 6.25 × height(cm) - 5 × age - 161
```

**Activity Multipliers:**

| Level | Multiplier |
|-------|------------|
| sedentary | 1.2 |
| light | 1.375 |
| moderate | 1.55 |
| active | 1.725 |
| very_active | 1.9 |

**Goal Adjustments:**

| Goal | Adjustment |
|------|------------|
| lose | -500 kcal |
| maintain | 0 |
| gain | +300 kcal |

**Macronutrient Split:**
- Protein: 1.0g per lb bodyweight
- Fat: 25% of total calories
- Carbs: Remaining calories

### Workout Generation

**Split Selection:**

| Days/Week | Split |
|-----------|-------|
| 3 | Full Body |
| 4 | Upper/Lower |
| 5 | Push/Pull/Legs |
| 6 | Push/Pull/Legs (2x) |

**Goal Parameters:**

| Goal | Reps | Sets | Rest (Compound) | RIR |
|------|------|------|-----------------|-----|
| strength | 3-6 | 4 | 180s | 1 |
| hypertrophy | 8-12 | 3 | 120s | 1 |
| endurance | 15-20 | 3 | 60s | 2 |
| weight_loss | 12-15 | 3 | 60s | 1 |

**Experience Multipliers:**

| Experience | Volume Multiplier |
|------------|-------------------|
| beginner | 0.85 |
| intermediate | 1.0 |
| advanced | 1.15 |

---

## Frontend Components

### Sections
1. **Navigation** - Fixed navbar with brand
2. **Hero** - CTA buttons for calculator and workout planner
3. **Calorie Calculator** - Unit toggle, form inputs, results display with macro cards
4. **Workout Planner** - Form inputs, workout plan display, exercise details
5. **Exercise Modal** - Exercise info and demonstration images

### Design System
- Primary: Indigo (#6366F1) → Purple (#8B5CF6) gradient
- Accent: Amber (#F59E0B)
- Success: Emerald (#10B981)
- Background: Light gray (#F8FAFC)
- Text: Dark gray (#1E293B)

---

## Configuration

### Server

| Setting | Value |
|---------|-------|
| Backend Port | 5000 |
| Frontend Port | 8000 |
| CORS | Enabled |

### Dependencies

```
Flask==3.0.0
flask-cors==4.0.0
```

---

## Exercise Database

### Muscle Groups

| Group | Count | Categories |
|-------|-------|------------|
| Chest | 8 | flat_press, incline_press, chest_fly, dip |
| Back | 6 | vertical_pull, horizontal_pull, isolation |
| Legs | 11 | squat, hip_hinge, quad_iso, hamstring_iso, unilateral |
| Shoulders | 5 | overhead_press, lateral_delt, rear_delt |
| Biceps | 3 | bicep_curl |
| Triceps | 3 | tricep_extension, tricep_press |
| Core | 2 | core |

### Exercise Schema

```json
{
  "id": 1,
  "name": "Barbell Bench Press",
  "muscle_group": "chest",
  "subcategory": "mid_chest",
  "equipment": ["barbell", "bench", "rack"],
  "difficulty": "intermediate",
  "type": "compound",
  "category": "flat_press",
  "rest": 120
}
```

---

## Data Storage

### Calorie Calculations Schema
```json
{
  "timestamp": "2025-01-15T10:30:00",
  "input": { "age": 30, "height": 175, "weight": 80, "gender": "male", "activity_level": "moderate", "goal": "lose" },
  "output": { "bmr": 1780, "tdee": 2759, "target_calories": 2259, "macros": {...} }
}
```

### Workout Plans Schema
```json
{
  "timestamp": "2025-01-15T10:30:00",
  "input": { "gender": "male", "goal": "hypertrophy", "experience": "intermediate", "equipment": [...], "days_per_week": 4 },
  "output": { "split": {...}, "workouts": [...], "progression": {...} }
}
```
