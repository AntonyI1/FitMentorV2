# Exercise Swap Feature

## Overview

Allow users to swap exercises in their generated workout plan with alternative exercises targeting the same muscle sub-region (e.g., swap one upper chest exercise for another upper chest exercise). The swap button appears subtly on each exercise item, opens a selection popup, and updates both the workout display and the exercise detail modal.

## User Stories

1. **As a user**, I want to swap an exercise for an alternative so I can use equipment I have available or prefer.
2. **As a user**, I want to see only exercises that target the same muscle area so my workout remains balanced.
3. **As a user**, I want the swap button to be unobtrusive so it doesn't clutter the interface.
4. **As a user**, I want to click on a swapped exercise and see its updated details in the modal.

## Acceptance Criteria

1. Each exercise item displays a swap button on the right side
2. Swap button has reduced opacity (faded) and does not dominate the UI
3. Swap button click opens a popup with alternative exercises
4. Alternatives are filtered by the same `sub_region` as the current exercise
5. Alternatives exclude the current exercise from the list
6. Selecting an alternative replaces the exercise in the workout display
7. Clicking on a swapped exercise opens the modal with the new exercise's details
8. Swap button click does NOT trigger the exercise detail modal
9. Pressing Escape or clicking outside the swap popup closes it
10. Swap popup displays exercise name, tier rating (if available), and difficulty

## Technical Requirements

### Frontend Components

**Swap Button (in exercise item)**
- Position: Right side of `.exercise-item`, before the details span
- Appearance: Icon (⇄ or similar), opacity 0.4, increases to 0.7 on hover
- Event: `click` with `stopPropagation()` to prevent modal trigger

**Swap Popup**
- Position: Anchored near the swap button (dropdown style)
- Content: List of alternative exercises with name, tier badge, difficulty
- Behavior: Click outside or Escape closes popup

### Data Requirements

**Exercise Cache Extension**
- Current `exercisesCache` already contains all exercises from `/api/exercises`
- Filter by `sub_region` to find alternatives
- Optionally filter by available equipment (from workout form data)

### State Management

- Store current workout plan data to allow modifications
- Track which exercise is being swapped (for popup positioning)
- Update rendered workout when swap occurs

### CSS Classes

- `.swap-btn` - The swap button
- `.swap-popup` - Popup container
- `.swap-popup-item` - Individual alternative in popup
- `.swap-popup-item:hover` - Hover state
- `.tier-badge` - Small badge showing Nippard tier

### API

No new endpoints required. Use existing:
- `GET /api/exercises` - Already cached in `exercisesCache`

## Dependencies

### Existing Code (will be modified)

| File | Changes |
|------|---------|
| `src/frontend/js/app.js` | Add swap button rendering, popup logic, event handlers |
| `src/frontend/css/styles.css` | Add styles for swap button and popup |
| `src/frontend/index.html` | Add swap popup HTML structure (if not generated dynamically) |

### Existing Functions

| Function | Relation |
|----------|----------|
| `renderWorkoutPlan()` | Add swap button to exercise item template |
| `showExerciseModal()` | Reuse for displaying swapped exercise details |
| `exercisesCache` | Filter to find alternatives |

## Edge Cases and Error States

| Scenario | Handling |
|----------|----------|
| No alternatives available | Show "No alternatives available" message in popup |
| Only one exercise in sub_region | Disable swap button or show message |
| Exercise not found in cache | Hide swap button for that exercise |
| Multiple popups open | Close any open popup before opening new one |
| Popup extends beyond viewport | Position popup above button if below viewport |
| Mobile/touch devices | Ensure popup is tap-friendly with adequate touch targets |

## UI Mockup (Text)

```
┌────────────────────────────────────────────────────────┐
│ Incline Barbell Bench Press    [⇄]  3 x 8-12 | 120s   │
└────────────────────────────────────────────────────────┘
                                  │
                                  ▼
                    ┌─────────────────────────────┐
                    │ Switch Exercise             │
                    ├─────────────────────────────┤
                    │ Incline Dumbbell Press  [A] │
                    │ Low-to-High Cable Fly       │
                    │ Incline Dumbbell Fly        │
                    │ Seated Cable Fly (Low)  [S] │
                    └─────────────────────────────┘
```

- `[⇄]` is the faded swap button
- `[A]` and `[S]` are tier badges
