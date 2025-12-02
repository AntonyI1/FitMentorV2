# Workout Planner - Implementation Plan

## Phase 1: Fix HTML ID Conflicts

**File:** `src/frontend/index.html`

**Tasks:**
1. Rename days per week select from `id="workout-days"` to `id="workout-days-select"`
2. Rename workout days container from `id="workout-days"` to `id="workout-days-list"`

**Changes:**
- Line 188: `<select id="workout-days-select" ...>`
- Line 253: `<div class="workout-days" id="workout-days-list"></div>`

## Phase 2: Update JavaScript Selectors

**File:** `src/frontend/js/app.js`

**Tasks:**
1. Update `getWorkoutFormData()` to use `#workout-days-select`
2. Update `renderWorkoutPlan()` to use `#workout-days-list`

**Changes:**
```javascript
// getWorkoutFormData()
days_per_week: parseInt($('#workout-days-select').value)

// renderWorkoutPlan()
const daysContainer = $('#workout-days-list');
```

## Phase 3: Verify Backend Integration

**File:** `src/backend/app.py`

**Tasks:**
1. Verify `/api/suggest-workout` endpoint returns correct structure
2. Confirm error handling returns proper JSON

**No changes expected** - backend implementation is correct.

## Phase 4: Manual Testing

**Tasks:**
1. Start servers with `python3 start.py`
2. Test workout form submission with various inputs
3. Verify results display correctly
4. Test exercise modal functionality
5. Verify form remains functional after generating plan
6. Test error states (no equipment, network error)

## Files to Modify

| File | Action |
|------|--------|
| `src/frontend/index.html` | Modify (2 lines) |
| `src/frontend/js/app.js` | Modify (2 lines) |

## Testing Strategy

1. **Form Functionality**
   - Fill form, submit, verify results appear
   - Change values, submit again, verify new results replace old
   - Verify days dropdown remains functional after submission

2. **Results Display**
   - Verify split name matches days_per_week selection
   - Verify exercises appear in each day card
   - Verify sets/reps/rest display correctly

3. **Modal Behavior**
   - Click exercise, verify modal opens
   - Test all close methods (X, overlay, Escape)

4. **Error Handling**
   - Submit with no equipment, verify error message
   - Stop backend, submit, verify connection error

## Complexity Estimate

**Low** - This is a 4-line fix for a duplicate ID bug. No architectural changes, no new features, just correcting element IDs and their corresponding selectors.
