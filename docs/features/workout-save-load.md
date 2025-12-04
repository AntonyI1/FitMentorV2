# Feature: Workout Save & Load

## Overview

Allow users to save generated workout plans with a name they choose and retrieve them later by entering that name. This enables users to return to their personalized workout without re-entering all their parameters. Simple persistence without user accounts - just a memorable name.

## User Stories

1. **As a user**, I want to save my generated workout plan with a name I choose so I can access it later.

2. **As a user**, I want to pick a name that's meaningful to me (my name, a nickname, "Tony's Plan") so I can easily remember it.

3. **As a user**, I want to load a previously saved workout by entering my chosen name so I can continue using my plan.

4. **As a user**, I want the save button to be visible but not distracting so I can save when ready without it cluttering the interface.

## Acceptance Criteria

### Save Functionality

- [ ] Save button appears after a workout is generated
- [ ] Save button is visible and obvious, but does not distract from the workout display
- [ ] Clicking save prompts user to enter a name (3-30 characters)
- [ ] Name is case-insensitive for lookup (stored lowercase)
- [ ] User receives confirmation that workout was saved successfully with their chosen name
- [ ] If name already exists, user is asked if they want to overwrite
- [ ] Saved workouts can be updated (save again with same name)

### Load Functionality

- [ ] Load option is accessible from the workout planner section before generating
- [ ] User can enter their name to retrieve their workout
- [ ] Name lookup is case-insensitive
- [ ] Invalid/unknown names show a clear error message
- [ ] Successfully loaded workouts display identically to freshly generated ones
- [ ] Loaded workouts can be modified (exercise swaps) and re-saved

### Data Persistence

- [ ] Workouts are stored in backend database (JSONL file)
- [ ] Each saved workout has: name, timestamp, workout data, input params
- [ ] Workouts persist across server restarts
- [ ] Saving with an existing name overwrites the previous workout

### Security (Lightweight)

- [ ] Names are normalized (trimmed, lowercased) for consistent lookup
- [ ] No personal data beyond the chosen name is stored
- [ ] No authentication - anyone who knows the name can load the workout
- [ ] Names must be alphanumeric with spaces/hyphens only (no special characters)

## Technical Requirements

### API Endpoints

#### POST /api/workouts/save

**Request:**
```json
{
  "name": "Tony's Workout",
  "workout": {
    "split": {...},
    "workouts": [...],
    "progression": {...}
  },
  "input_params": {
    "gender": "male",
    "goal": "hypertrophy",
    "experience": "intermediate",
    "equipment": [...],
    "days_per_week": 4,
    "session_duration": 60
  }
}
```

**Response (Success):**
```json
{
  "success": true,
  "name": "tonys workout",
  "message": "Workout saved successfully",
  "overwritten": false
}
```

**Response (Overwrite):**
```json
{
  "success": true,
  "name": "tonys workout",
  "message": "Workout updated successfully",
  "overwritten": true
}
```

**Response (Error):**
```json
{
  "success": false,
  "error": "Name must be 3-30 characters"
}
```

#### GET /api/workouts/load/<name>

**Response (Success):**
```json
{
  "success": true,
  "name": "tonys workout",
  "workout": {
    "split": {...},
    "workouts": [...],
    "progression": {...}
  },
  "input_params": {...},
  "saved_at": "2025-01-15T10:30:00"
}
```

**Response (Not Found):**
```json
{
  "success": false,
  "error": "No workout found with that name"
}
```

#### GET /api/workouts/exists/<name>

Check if a name already exists (for overwrite confirmation).

**Response:**
```json
{
  "exists": true,
  "saved_at": "2025-01-15T10:30:00"
}
```

### Data Model

#### saved_workouts.jsonl

```json
{
  "name": "tonys workout",
  "saved_at": "2025-01-15T10:30:00",
  "input_params": {
    "gender": "male",
    "goal": "hypertrophy",
    "experience": "intermediate",
    "equipment": ["barbell", "dumbbell", "cable", "bench", "rack"],
    "days_per_week": 4,
    "session_duration": 60
  },
  "workout": {
    "split": {...},
    "workouts": [...],
    "progression": {...}
  }
}
```

### Backend Components

| File | Changes |
|------|---------|
| `app.py` | Add `/api/workouts/save`, `/api/workouts/load/<name>`, `/api/workouts/exists/<name>` |
| `models/workout_storage.py` | New module for save/load/exists logic and name normalization |
| `data/saved_workouts.jsonl` | New data file for saved workouts |

### Frontend Components

| File | Changes |
|------|---------|
| `index.html` | Add save button to workout results, add load workout UI section |
| `js/app.js` | Add `saveWorkout()`, `loadWorkout()`, `checkNameExists()` functions |
| `css/styles.css` | Styles for save button, save modal, load form |

### UI Placement

**Save Button:**
- Position: Top-right corner of workout results header
- Style: Secondary/outline button, not the primary CTA color
- Text: "Save Workout"
- Click behavior: Opens small modal/inline form to enter name

**Save Modal/Form:**
- Input field for name with placeholder "Enter a name (e.g., your name)"
- Character count indicator
- Save and Cancel buttons
- Shows success message with the saved name

**Load Workout:**
- Position: Within workout planner section, above the generate form
- Style: Subtle link or collapsible section
- Text: "Load a saved workout"
- Collapsed by default, expands to show input field
- Input placeholder: "Enter your workout name"

## Dependencies

### Existing Code

| File | Dependency |
|------|------------|
| `app.py` | Add routes alongside existing endpoints |
| `data_collector.py` | Reference for JSONL patterns (append, read) |
| `app.js` | Extend `currentWorkoutData` handling |
| `styles.css` | Use existing button, form, and modal styles |

### New Files

| File | Purpose |
|------|---------|
| `models/workout_storage.py` | Encapsulate save/load/exists logic |
| `data/saved_workouts.jsonl` | Persist saved workouts |

## Edge Cases and Error States

### Save Errors

| Scenario | Handling |
|----------|----------|
| No workout generated yet | Save button not visible |
| Name too short (<3 chars) | Show validation error |
| Name too long (>30 chars) | Truncate input or show error |
| Invalid characters in name | Show validation error, explain allowed chars |
| Server error during save | Show error toast, allow retry |
| Name already exists | Show confirmation dialog asking to overwrite |

### Load Errors

| Scenario | Handling |
|----------|----------|
| Name not found | Clear message: "No workout found with that name" |
| Empty name submitted | Disable submit until name entered |
| Server error | Show error message, allow retry |

### Data Edge Cases

| Scenario | Handling |
|----------|----------|
| JSONL file doesn't exist | Create on first save |
| Malformed JSONL line | Skip during read, log warning |
| Same name saved twice | Update existing record (overwrite) |
| Concurrent saves with same name | Last write wins |

### UI Edge Cases

| Scenario | Handling |
|----------|----------|
| User saves, then modifies workout | Can save again (same or different name) |
| User loads workout, then generates new one | New workout replaces loaded, can save separately |
| Mobile viewport | Ensure save button and load form are accessible |
| User forgets their name | No recovery mechanism (by design) |

## Out of Scope

- User accounts and authentication
- Password protection for workouts
- Workout expiration/auto-deletion
- Listing all saved workouts (just direct lookup by name)
- Sharing via URL
- Workout history for a name
- Rate limiting
- Encryption of stored data
