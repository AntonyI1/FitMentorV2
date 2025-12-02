# Backend API

## Overview

Flask-based REST API server that provides calorie calculation and workout plan generation endpoints. Serves as the core backend for the FitMentor application with JSON Lines data persistence.

## User Stories

- As a user, I can send my physical stats and receive calculated calorie/macro targets
- As a user, I can request a personalized workout plan based on my goals and equipment
- As a user, I can browse the exercise database
- As a developer, I can start the server with a single command

## Acceptance Criteria

- [ ] Server starts on port 5000 with `python run.py` from project root
- [ ] GET `/` returns API info and version
- [ ] POST `/api/calculate-calories` accepts valid input and returns BMR, TDEE, target calories, and macros
- [ ] POST `/api/suggest-workout` accepts valid input and returns split, workouts, and progression
- [ ] GET `/api/exercises` returns the complete exercise database
- [ ] GET `/api/stats` returns data collection statistics
- [ ] Invalid requests return appropriate error responses (400)
- [ ] CORS is enabled for frontend integration
- [ ] All calculations are logged to JSONL files

## Technical Requirements

### Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | API info |
| POST | `/api/calculate-calories` | Calorie calculation |
| POST | `/api/suggest-workout` | Workout generation |
| GET | `/api/exercises` | Exercise database |
| GET | `/api/stats` | Collection stats |

### Models

1. **calorie_calculator.py** - Mifflin-St Jeor equation, activity multipliers, goal adjustments, macro calculation
2. **workout_suggester.py** - Split selection, exercise database, workout generation, progression strategies
3. **data_collector.py** - JSONL read/write operations

### Data Files

- `src/backend/data/calorie_calculations.jsonl`
- `src/backend/data/workout_plans.jsonl`

## Dependencies

- Flask 3.0.0
- flask-cors 4.0.0
- Existing project structure in `src/backend/`

## Edge Cases and Error States

| Scenario | Response |
|----------|----------|
| Missing required field | 400 with field name |
| Value out of range (age, height, weight) | 400 with valid range |
| Invalid enum value | 400 with valid options |
| Invalid JSON body | 400 with parse error |
| No exercises match equipment | Return bodyweight alternatives |
| Data file doesn't exist | Create on first write |
