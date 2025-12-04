# Exercise Remove Feature

## Overview

Allow users to remove exercises from their generated workout plan. When the remove button is clicked, a confirmation dialog prompts the user before deletion. The removed exercise is excluded from the workout data, and when the workout is saved, the removed exercise is not persisted.

## User Stories

1. **As a user**, I want to remove an exercise from my workout so I can customize my plan to my needs.
2. **As a user**, I want a confirmation prompt before removing an exercise so I don't accidentally delete exercises.
3. **As a user**, I want the remove action to be reflected immediately in my workout display.
4. **As a user**, I want my saved workout to exclude any exercises I removed.

## Acceptance Criteria

1. Each exercise item displays a remove button (trash icon or "X")
2. Remove button has reduced opacity (faded) to match the swap button styling
3. Clicking the remove button opens a confirmation dialog
4. Confirmation dialog displays the exercise name being removed
5. Confirmation dialog has "Cancel" and "Remove" buttons
6. Clicking "Cancel" closes the dialog without removing the exercise
7. Clicking "Remove" removes the exercise from the workout data and display
8. Remove button click does NOT trigger the exercise detail modal
9. Pressing Escape closes the confirmation dialog without removing
10. Saved workout does not include removed exercises
11. If all exercises are removed from a day, the day shows an empty state message

## Technical Requirements

### Frontend Components

**Remove Button (in exercise item)**
- Position: Right side of `.exercise-item`, next to swap button
- Appearance: Icon (✕ or trash icon), opacity 0.4, increases to 0.7 on hover
- Event: `click` with `stopPropagation()` to prevent modal trigger

**Confirmation Modal**
- Structure: Reuse existing modal pattern (overlay + content)
- Content: Warning text with exercise name, Cancel and Remove buttons
- Styling: Remove button in red/danger color to indicate destructive action
- Behavior: Click overlay or Escape closes without action

### Data Requirements

- No new data required
- Uses existing `currentWorkoutData` which is modified in-place
- When `saveWorkoutAPI()` is called, it sends the modified workout data (without removed exercises)

### State Management

- Track which exercise removal is pending (for confirmation dialog)
- Update `currentWorkoutData` when removal is confirmed
- Re-render workout plan after removal

### CSS Classes

- `.remove-btn` - The remove button
- `.confirm-modal` - Confirmation modal container
- `.confirm-modal-content` - Modal content area
- `.confirm-message` - The confirmation text
- `.confirm-exercise-name` - Highlighted exercise name in message
- `.confirm-actions` - Container for buttons
- `.btn-cancel` - Cancel button
- `.btn-danger` - Red/danger styled remove button

### API

No new endpoints required. Uses existing:
- `POST /api/workouts/save` - Already handles modified workout data

### HTML Structure

```html
<!-- Confirmation Modal -->
<div id="confirm-modal" class="modal" style="display: none;">
    <div class="modal-overlay"></div>
    <div class="confirm-modal-content">
        <p class="confirm-message">
            Are you sure you want to remove
            <strong id="confirm-exercise-name"></strong>?
        </p>
        <div class="confirm-actions">
            <button id="confirm-cancel" class="btn btn-secondary">Cancel</button>
            <button id="confirm-remove" class="btn btn-danger">Remove</button>
        </div>
    </div>
</div>
```

## Dependencies

### Existing Code (will be modified)

| File | Changes |
|------|---------|
| `src/frontend/js/app.js` | Add remove button rendering, confirmation dialog logic, event handlers, removal function |
| `src/frontend/css/styles.css` | Add styles for remove button, confirmation modal, danger button |
| `src/frontend/index.html` | Add confirmation modal HTML structure |

### Existing Functions

| Function | Relation |
|----------|----------|
| `renderWorkoutPlan()` | Add remove button to exercise item template |
| `swapExercise()` | Pattern reference for modifying workout data and re-rendering |
| `hideSwapPopup()` | Pattern reference for closing popups on escape/outside click |
| `currentWorkoutData` | Will be modified when exercise is removed |
| `saveWorkoutAPI()` | Will save the modified workout data (already handles this correctly) |

## Edge Cases and Error States

| Scenario | Handling |
|----------|----------|
| Remove last exercise in a day | Show "No exercises" message in that day |
| User clicks outside confirmation dialog | Close dialog, do not remove |
| User presses Escape during confirmation | Close dialog, do not remove |
| Multiple rapid clicks on remove | Ignore clicks while confirmation dialog is open |
| Exercise already removed (stale UI) | Gracefully handle by checking if exercise exists |
| Workout is saved while confirmation open | Close confirmation first, then proceed with save |

## UI Mockup (Text)

```
┌────────────────────────────────────────────────────────────────┐
│ Incline Barbell Bench Press    [⇄] [✕]  3 x 8-12 | 120s       │
└────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼ (on ✕ click)
                    ┌─────────────────────────────────┐
                    │                                 │
                    │  Are you sure you want to       │
                    │  remove Incline Barbell         │
                    │  Bench Press?                   │
                    │                                 │
                    │     [Cancel]    [Remove]        │
                    │                                 │
                    └─────────────────────────────────┘
```

- `[✕]` is the faded remove button next to swap button
- `[Remove]` button is styled in red/danger color
