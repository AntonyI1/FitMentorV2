# Backend API - Implementation Plan

## Phase 1: Project Setup ✓

**Files created:**
- `start.py` (project root) - Starts both backend and frontend servers
- `requirements.txt` (project root) - Dependencies

**Tasks (completed):**
1. Created `start.py` that starts Flask backend and Python HTTP server for frontend
2. Created `requirements.txt` with Flask

## Phase 2: Exercise Database

**Files to create:**
- `src/backend/models/exercises.py` - Exercise data and lookup functions

**Tasks:**
1. Define all 38 exercises with full metadata
2. Create functions: `get_all_exercises()`, `get_exercises_by_muscle_group()`, `get_exercises_by_equipment()`

## Phase 3: Calorie Calculator Model

**Files to create:**
- `src/backend/models/calorie_calculator.py`

**Tasks:**
1. Implement Mifflin-St Jeor BMR calculation
2. Implement TDEE calculation with activity multipliers
3. Implement goal adjustments
4. Implement macro calculation (protein 1g/lb, fat 25%, carbs remainder)
5. Add input validation

## Phase 4: Workout Suggester Model

**Files to create:**
- `src/backend/models/workout_suggester.py`

**Tasks:**
1. Define training splits (Full Body, Upper/Lower, PPL)
2. Implement split selection based on days_per_week
3. Implement exercise selection logic (filter by equipment, balance muscle groups)
4. Implement goal-specific parameters (reps, sets, rest)
5. Implement progression strategies
6. Add input validation

## Phase 5: Data Collector Model

**Files to create:**
- `src/backend/models/data_collector.py`

**Tasks:**
1. Implement JSONL append function
2. Implement JSONL read function
3. Implement stats aggregation
4. Handle file creation on first write

## Phase 6: Flask Application

**Files to modify:**
- `src/backend/app.py`

**Tasks:**
1. Initialize Flask app with CORS
2. Implement GET `/` endpoint
3. Implement POST `/api/calculate-calories` endpoint
4. Implement POST `/api/suggest-workout` endpoint
5. Implement GET `/api/exercises` endpoint
6. Implement GET `/api/stats` endpoint
7. Add error handling middleware

## API Contracts

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
    "protein": {"grams": 176, "calories": 704, "percentage": 31},
    "carbs": {"grams": 226, "calories": 904, "percentage": 40},
    "fats": {"grams": 62, "calories": 558, "percentage": 25}
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
    "name": "Upper/Lower",
    "days": [...]
  },
  "workouts": [...],
  "progression": {...}
}
```

## Testing Strategy

1. Manual API testing with curl/httpie after each phase
2. Test edge cases: missing fields, invalid values, empty equipment list

## Complexity Estimate

**Medium** - Well-defined requirements, standard Flask patterns, no external dependencies beyond Flask.
