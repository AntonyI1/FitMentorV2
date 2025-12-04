# Implementation Plan: Workout Save & Load

## Overview

Add the ability to save workout plans with a user-chosen name and load them later. Uses existing JSONL patterns for persistence.

**Complexity:** Low-Medium

---

## Phase 1: Backend Storage Module

Create the `workout_storage.py` module following existing `data_collector.py` patterns.

### Files to Create

| File | Purpose |
|------|---------|
| `src/backend/models/workout_storage.py` | Save/load/exists logic, name normalization |

### Implementation

**workout_storage.py:**

```python
# Functions needed:
- normalize_name(name) -> str
  # Trim, lowercase, validate (3-30 chars, alphanumeric + spaces/hyphens)

- validate_name(name) -> tuple[bool, str]
  # Returns (is_valid, error_message)

- save_workout(name, workout, input_params) -> dict
  # Check exists, write/overwrite to JSONL, return success response

- load_workout(name) -> dict | None
  # Read JSONL, find by normalized name, return workout or None

- workout_exists(name) -> dict
  # Return {exists: bool, saved_at: str | None}
```

**Data file:** `src/backend/data/saved_workouts.jsonl`
- Created automatically on first save
- One JSON record per line
- Records contain: name, saved_at, input_params, workout

**Name handling:**
- Stored lowercase with spaces preserved
- "Tony's Workout" → "tonys workout" (apostrophe removed)
- Lookup is case-insensitive

---

## Phase 2: Backend API Endpoints

Add three endpoints to `app.py`.

### Files to Modify

| File | Changes |
|------|---------|
| `src/backend/app.py` | Add 3 routes, import workout_storage |

### Endpoints

**POST /api/workouts/save**
- Request: `{ name, workout, input_params }`
- Validate name
- Call `workout_storage.save_workout()`
- Return: `{ success, name, message, overwritten }`

**GET /api/workouts/load/<name>**
- URL-decode the name parameter
- Call `workout_storage.load_workout()`
- Return workout data or 404 error

**GET /api/workouts/exists/<name>**
- URL-decode the name parameter
- Call `workout_storage.workout_exists()`
- Return: `{ exists, saved_at }`

### Integration Points

- Add import: `from models import workout_storage`
- Add to endpoint list in index route
- Follow existing error handling patterns (try/except, 400/404 responses)

---

## Phase 3: Frontend - Save Functionality

Add save button and modal to workout results.

### Files to Modify

| File | Changes |
|------|---------|
| `src/frontend/index.html` | Save button in results header, save modal |
| `src/frontend/js/app.js` | Save functions and handlers |
| `src/frontend/css/styles.css` | Save button and modal styles |

### HTML Changes

**Workout results header** (modify `#workout-results`):
- Add save button with text "Save Workout"
- Position: right side of `.split-overview` header

**Save modal** (new element after `#swap-popup`):
```html
<div id="save-modal" class="modal" style="display: none;">
  <div class="modal-overlay"></div>
  <div class="modal-content">
    <button class="modal-close">&times;</button>
    <h3>Save Workout</h3>
    <form id="save-workout-form">
      <div class="form-group">
        <label>Enter a name for your workout</label>
        <input type="text" id="save-name" placeholder="e.g., Tony" minlength="3" maxlength="30" required>
        <div class="char-count"><span id="name-char-count">0</span>/30</div>
      </div>
      <div id="save-exists-warning" style="display: none;">
        A workout with this name exists. Save will overwrite it.
      </div>
      <div class="modal-buttons">
        <button type="button" class="btn btn-secondary" id="save-cancel">Cancel</button>
        <button type="submit" class="btn btn-primary">Save</button>
      </div>
    </form>
    <div id="save-success" style="display: none;">
      Saved as "<span id="saved-name"></span>"
    </div>
  </div>
</div>
```

### JavaScript Changes

**New API functions:**
```javascript
async function saveWorkoutAPI(name, workout, inputParams) { ... }
async function loadWorkoutAPI(name) { ... }
async function checkNameExists(name) { ... }
```

**New handler functions:**
```javascript
function showSaveModal() { ... }
function hideSaveModal() { ... }
async function handleSaveSubmit(e) { ... }
function updateCharCount() { ... }
```

**State additions:**
```javascript
let currentInputParams = null;  // Store input params when generating workout
```

**Modifications:**
- Update `handleWorkoutSubmit()` to store input params
- Add event listeners in DOMContentLoaded

### CSS Changes

**Save button styling:**
```css
.save-btn { ... }  /* Secondary/outline style, positioned in split-overview */
```

**Modal additions:**
```css
.modal-buttons { ... }  /* Flex row for Cancel/Save buttons */
.char-count { ... }     /* Small text showing character count */
.save-exists-warning { ... }  /* Warning message styling */
.save-success { ... }   /* Success message styling */
```

---

## Phase 4: Frontend - Load Functionality

Add load section above workout form.

### HTML Changes

**Load section** (add above `#workout-form`):
```html
<div class="load-workout-toggle">
  <button type="button" id="load-toggle">Have a saved workout? Load it</button>
</div>
<div id="load-workout-form" style="display: none;">
  <div class="form-group">
    <label>Enter your workout name</label>
    <div class="load-input-row">
      <input type="text" id="load-name" placeholder="e.g., Tony">
      <button type="button" class="btn btn-primary" id="load-btn">Load</button>
    </div>
  </div>
  <div id="load-error" class="form-error" style="display: none;"></div>
</div>
```

### JavaScript Changes

**New functions:**
```javascript
function toggleLoadForm() { ... }
async function handleLoadWorkout() { ... }
```

**Event listeners:**
- Toggle button click
- Load button click
- Enter key in load input

**Behavior:**
- On successful load, populate `currentWorkoutData` and `currentInputParams`
- Call `renderWorkoutPlan()` to display
- Scroll to results

### CSS Changes

```css
.load-workout-toggle { ... }  /* Centered, subtle link style */
.load-input-row { ... }       /* Input + button row */
```

---

## File Summary

### New Files

| File | Lines (est) |
|------|-------------|
| `src/backend/models/workout_storage.py` | ~80 |

### Modified Files

| File | Changes |
|------|---------|
| `src/backend/app.py` | +40 lines (3 endpoints) |
| `src/frontend/index.html` | +40 lines (modal, load section) |
| `src/frontend/js/app.js` | +100 lines (API, handlers, state) |
| `src/frontend/css/styles.css` | +60 lines (save modal, load section) |

---

## API Contracts

### POST /api/workouts/save

**Request:**
```json
{
  "name": "Tony's Workout",
  "workout": {
    "split": { "name": "Upper/Lower", "days": [...] },
    "workouts": [...],
    "progression": { "method": "...", "increment": "...", "deload": "..." }
  },
  "input_params": {
    "gender": "male",
    "goal": "hypertrophy",
    "experience": "intermediate",
    "equipment": ["barbell", "dumbbell"],
    "days_per_week": 4,
    "session_duration": 60
  }
}
```

**Response (201):**
```json
{
  "success": true,
  "name": "tonys workout",
  "message": "Workout saved successfully",
  "overwritten": false
}
```

**Response (400):**
```json
{
  "success": false,
  "error": "Name must be 3-30 characters"
}
```

### GET /api/workouts/load/<name>

**Response (200):**
```json
{
  "success": true,
  "name": "tonys workout",
  "workout": { ... },
  "input_params": { ... },
  "saved_at": "2025-01-15T10:30:00"
}
```

**Response (404):**
```json
{
  "success": false,
  "error": "No workout found with that name"
}
```

### GET /api/workouts/exists/<name>

**Response (200):**
```json
{
  "exists": true,
  "saved_at": "2025-01-15T10:30:00"
}
```

---

## Data Model

### saved_workouts.jsonl

Each line is a complete JSON record:

```json
{"name": "tonys workout", "saved_at": "2025-01-15T10:30:00", "input_params": {...}, "workout": {...}}
```

**Fields:**
- `name` (string): Normalized name (lowercase, no special chars except spaces/hyphens)
- `saved_at` (string): ISO timestamp
- `input_params` (object): Original form inputs
- `workout` (object): Complete workout plan data

**Overwrite behavior:**
When saving with an existing name, the old record is replaced (rewrite entire file with updated record).

---

## Component Hierarchy

```
index.html
├── #workout-section
│   ├── .load-workout-toggle (new)
│   │   └── #load-toggle button
│   ├── #load-workout-form (new, hidden)
│   │   ├── #load-name input
│   │   ├── #load-btn button
│   │   └── #load-error
│   ├── #workout-form (existing)
│   └── #workout-results (existing)
│       └── .split-overview
│           └── .save-btn (new)
└── #save-modal (new)
    └── .modal-content
        ├── #save-workout-form
        │   ├── #save-name input
        │   ├── #save-exists-warning
        │   └── buttons
        └── #save-success
```

---

## Testing Strategy

### Backend Tests

**Unit tests for workout_storage.py:**
- `test_normalize_name()` - various inputs
- `test_validate_name()` - valid/invalid cases
- `test_save_workout()` - new save
- `test_save_workout_overwrite()` - existing name
- `test_load_workout()` - existing/missing
- `test_workout_exists()` - true/false cases

**Integration tests for endpoints:**
- Save new workout
- Save overwrites existing
- Load existing workout
- Load missing returns 404
- Check exists true/false
- Invalid name validation

### Frontend Tests (Manual)

- Generate workout, save with name
- Load saved workout by name
- Overwrite existing name
- Load non-existent name (error)
- Character count updates
- Modal open/close
- Load section toggle
- Loaded workout can be modified and re-saved

### Edge Cases to Test

- Name with spaces: "My Workout"
- Name with hyphens: "tony-workout"
- Name at limits: "abc" (3 chars), 30 char name
- Case insensitivity: save "Tony", load "TONY"
- Special characters rejected: "Tony's" → error or strip
- Empty name: validation error
- Name too short/long: validation error

---

## Implementation Order

1. **Phase 1:** Create `workout_storage.py` with all functions
2. **Phase 2:** Add API endpoints to `app.py`
3. **Phase 3:** Add save button, modal, and JS handlers
4. **Phase 4:** Add load section and handlers
5. **Testing:** Manual end-to-end testing
