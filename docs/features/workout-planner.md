# Workout Planner - Feature Document

## Overview

The workout planner generates personalized multi-day training programs based on user parameters (goal, experience, equipment, training frequency). It selects appropriate exercises from a 38-exercise database, applies goal-specific training parameters, and displays the complete plan with progression guidelines.

## User Stories

1. As a user, I want to select my training goal so the plan matches my objectives
2. As a user, I want to specify my available equipment so exercises are feasible
3. As a user, I want to choose my training frequency so the split fits my schedule
4. As a user, I want to see detailed workouts with sets, reps, and rest periods
5. As a user, I want to click exercises to see more details
6. As a user, I want to generate multiple plans without refreshing the page

## Acceptance Criteria

1. **Form Submission**
   - Form validates all required fields before submission
   - At least one equipment option must be selected
   - Loading state shows during API call
   - Form remains functional after displaying results

2. **Plan Display**
   - Split name and progression method display correctly
   - Each training day shows with muscle groups
   - Each exercise shows name, sets, reps, and rest period
   - Results scroll into view smoothly

3. **Exercise Modal**
   - Clicking an exercise opens modal with details
   - Modal shows: muscle group, type, difficulty, equipment, rest
   - Modal closes via X button, overlay click, or Escape key

4. **Error Handling**
   - Network errors display user-friendly message
   - Validation errors from backend display correctly
   - Form remains usable after errors

5. **Repeat Usage**
   - User can change inputs and generate a new plan
   - Previous results are replaced, not appended
   - Form values persist (not reset) after generation

## Technical Requirements

### Backend Endpoint

**POST /api/suggest-workout**

Request:
```json
{
  "gender": "male|female",
  "goal": "strength|hypertrophy|endurance|weight_loss",
  "experience": "beginner|intermediate|advanced",
  "equipment": ["barbell", "dumbbell", ...],
  "days_per_week": 3-6,
  "session_duration": 30-120
}
```

Response:
```json
{
  "split": {
    "name": "Upper/Lower 4x/week",
    "days": [{"name": "Upper A", "muscle_groups": [...]}]
  },
  "workouts": [{
    "day": "Upper A",
    "muscle_groups": ["chest", "back", ...],
    "exercises": [{
      "name": "Barbell Bench Press",
      "sets": 3,
      "reps": "8-12",
      "rest_seconds": 120
    }]
  }],
  "progression": {
    "method": "Double Progression",
    "increment": "...",
    "deload": "..."
  }
}
```

### Frontend Components

1. **Workout Form** (`#workout-form`)
   - Gender select
   - Goal select
   - Experience select
   - Equipment checkbox grid
   - Days per week select
   - Submit button with loading spinner

2. **Results Display** (`#workout-results`)
   - Split overview card with progression info
   - Day cards with exercise lists
   - Exercise items (clickable)

3. **Exercise Modal** (`#exercise-modal`)
   - Overlay backdrop
   - Content card with exercise details

### DOM Element IDs

Form elements:
- `#workout-form` - form container
- `#workout-gender` - gender select
- `#workout-goal` - goal select
- `#workout-experience` - experience select
- `#workout-days-select` - days per week select (UNIQUE ID)
- `input[name="equipment"]` - equipment checkboxes

Results elements:
- `#workout-results` - results container
- `#split-name` - split name display
- `#progression-method` - progression method
- `#progression-details` - progression details
- `#workout-days-list` - container for day cards (UNIQUE ID)

Modal elements:
- `#exercise-modal` - modal container
- `#modal-exercise-name` - exercise name
- `#modal-muscle-group`, `#modal-type`, `#modal-difficulty`, `#modal-equipment`, `#modal-rest`

## Dependencies

- Backend: `src/backend/models/workout_suggester.py`
- Backend: `src/backend/models/exercises.py`
- Backend: `src/backend/app.py` (endpoint handler)
- Frontend: `src/frontend/index.html`
- Frontend: `src/frontend/js/app.js`
- Frontend: `src/frontend/css/styles.css`

## Edge Cases and Error States

1. **No equipment selected** - Show error "Please select at least one equipment option"
2. **Backend unreachable** - Show error "Cannot connect to server"
3. **Invalid input** - Display backend validation error message
4. **No exercises match equipment** - Backend falls back to bodyweight exercises
5. **Empty exercises cache** - Modal shows without full details (graceful degradation)

