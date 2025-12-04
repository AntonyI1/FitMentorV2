# Exercise Remove Implementation Plan

## Summary

Add the ability to remove exercises from a workout plan with a confirmation dialog. This is a low-complexity feature that follows existing patterns (swap button, modal dialogs) already in the codebase.

## Complexity Estimate

**Low** - Uses existing patterns for buttons, modals, and data modification. No backend changes required.

---

## Phases

### Phase 1: Add Confirmation Modal HTML

**File:** `src/frontend/index.html`

**Changes:**
Add confirmation modal structure after the save modal (line 339):

```html
<div id="confirm-remove-modal" class="modal" style="display: none;">
    <div class="modal-overlay"></div>
    <div class="modal-content confirm-modal-content">
        <p class="confirm-message">
            Are you sure you want to remove
            <strong id="confirm-exercise-name"></strong>?
        </p>
        <div class="confirm-actions">
            <button type="button" class="btn btn-secondary" id="confirm-cancel">Cancel</button>
            <button type="button" class="btn btn-danger" id="confirm-remove">Remove</button>
        </div>
    </div>
</div>
```

---

### Phase 2: Add CSS Styles

**File:** `src/frontend/css/styles.css`

**Changes:**

1. Add `.remove-btn` styles (after `.swap-btn` styles, ~line 604):
```css
.remove-btn {
    background: none;
    border: none;
    font-size: 14px;
    cursor: pointer;
    opacity: 0.4;
    padding: 4px 8px;
    margin-right: 12px;
    transition: opacity 0.2s;
    color: inherit;
    flex-shrink: 0;
}

.remove-btn:hover {
    opacity: 0.8;
    color: var(--error);
}

.exercise-item:hover .remove-btn {
    opacity: 0.7;
}

.exercise-item:hover .remove-btn:hover {
    opacity: 1;
    color: #FCA5A5;
}
```

2. Add `.btn-danger` style (after `.btn-secondary`, ~line 127):
```css
.btn-danger {
    background: var(--error);
    color: white;
}

.btn-danger:hover {
    background: #DC2626;
    transform: translateY(-2px);
}
```

3. Add confirmation modal styles (after save modal styles, ~line 900):
```css
.confirm-modal-content {
    max-width: 320px;
    text-align: center;
    padding: 32px 24px;
}

.confirm-message {
    font-size: 16px;
    margin-bottom: 24px;
    line-height: 1.5;
}

.confirm-message strong {
    color: var(--primary);
    display: block;
    margin-top: 4px;
}

.confirm-actions {
    display: flex;
    gap: 12px;
    justify-content: center;
}

.confirm-actions .btn {
    padding: 10px 24px;
}
```

4. Add empty state style for days with no exercises:
```css
.exercise-list-empty {
    padding: 24px;
    text-align: center;
    color: var(--text-light);
    font-size: 14px;
    font-style: italic;
}
```

---

### Phase 3: Add JavaScript Logic

**File:** `src/frontend/js/app.js`

**Changes:**

1. Add state variable (after `activeSwapContext`, line 7):
```javascript
let pendingRemoval = null; // { dayIndex, exerciseIndex, exerciseName }
```

2. Modify `renderWorkoutPlan()` (line 151-195):
   - Add remove button next to swap button in the exercise item template
   - Add empty state handling when no exercises exist
   - Add click handlers for remove buttons

Template change (inside the map for exercises):
```javascript
<button class="remove-btn" title="Remove exercise">✕</button>
```

3. Add new functions after `swapExercise()` (line 295):

```javascript
// Confirmation modal functions
function showConfirmRemoveModal(exerciseName, dayIndex, exerciseIndex) {
    pendingRemoval = { dayIndex, exerciseIndex, exerciseName };
    $('#confirm-exercise-name').textContent = exerciseName;
    show('#confirm-remove-modal');
}

function hideConfirmRemoveModal() {
    hide('#confirm-remove-modal');
    pendingRemoval = null;
}

function removeExercise() {
    if (!pendingRemoval) return;

    const { dayIndex, exerciseIndex } = pendingRemoval;
    const workout = currentWorkoutData.workouts[dayIndex];

    // Remove exercise from array
    workout.exercises.splice(exerciseIndex, 1);

    // Re-render the workout plan
    renderWorkoutPlan(currentWorkoutData);
    hideConfirmRemoveModal();
}
```

4. Update event listeners in `DOMContentLoaded` (after line 630):
```javascript
// Confirm remove modal
$('#confirm-remove-modal .modal-overlay').addEventListener('click', hideConfirmRemoveModal);
$('#confirm-cancel').addEventListener('click', hideConfirmRemoveModal);
$('#confirm-remove').addEventListener('click', removeExercise);
```

5. Update Escape key handler (line 626-631):
```javascript
if (e.key === 'Escape') {
    hideExerciseModal();
    hideSaveModal();
    hideSwapPopup();
    hideConfirmRemoveModal();
}
```

---

## Files to Modify

| File | Type | Changes |
|------|------|---------|
| `src/frontend/index.html` | Modify | Add confirmation modal HTML |
| `src/frontend/css/styles.css` | Modify | Add remove button, danger button, confirmation modal styles |
| `src/frontend/js/app.js` | Modify | Add state variable, modify renderWorkoutPlan, add modal functions and event handlers |

---

## Data Models / Schema Changes

None. The feature modifies `currentWorkoutData` in-place using `Array.splice()`. When the workout is saved via `saveWorkoutAPI()`, it sends the modified data which excludes removed exercises.

---

## API Contracts

No new API endpoints. Uses existing:
- `POST /api/workouts/save` - Already handles any workout data structure

---

## Component Hierarchy

```
index.html
├── #confirm-remove-modal (NEW)
│   ├── .modal-overlay
│   └── .confirm-modal-content
│       ├── .confirm-message
│       │   └── #confirm-exercise-name
│       └── .confirm-actions
│           ├── #confirm-cancel (.btn-secondary)
│           └── #confirm-remove (.btn-danger)
└── .exercise-item (MODIFIED)
    ├── .exercise-name
    ├── .swap-btn (existing)
    ├── .remove-btn (NEW)
    └── .exercise-details
```

---

## Testing Strategy

### Manual Testing

1. **Remove button visibility**
   - Generate a workout plan
   - Verify each exercise shows both swap (⇄) and remove (✕) buttons
   - Verify buttons are faded and become more visible on hover

2. **Confirmation dialog**
   - Click remove button
   - Verify dialog appears with correct exercise name
   - Verify Cancel and Remove buttons are visible
   - Verify Remove button is red/danger colored

3. **Cancel behavior**
   - Click Cancel in dialog → dialog closes, exercise remains
   - Click overlay → dialog closes, exercise remains
   - Press Escape → dialog closes, exercise remains

4. **Remove behavior**
   - Click Remove → exercise is removed from display
   - Verify workout data is updated (exercise count decreases)

5. **Save after remove**
   - Remove an exercise
   - Save the workout
   - Load the workout
   - Verify removed exercise is not present

6. **Empty day handling**
   - Remove all exercises from one day
   - Verify "No exercises" message appears

7. **Rapid actions**
   - While confirmation dialog is open, try clicking another remove button
   - Verify only one dialog is open at a time

8. **Mobile/touch**
   - Verify buttons have adequate touch targets
   - Verify dialog is properly centered and sized on mobile

### Edge Cases to Verify

- Remove last exercise in a day → shows empty state
- Remove while swap popup is open → swap popup closes
- Press Escape during confirmation → closes confirmation only
- Click remove on same exercise twice rapidly → no errors
