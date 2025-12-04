# Exercise Swap Implementation Plan

## Overview

Implement the exercise swap feature as defined in `/docs/features/exercise-swap.md`. This is a frontend-only feature that uses the existing exercise cache.

## Complexity Estimate

**Medium** - Requires DOM manipulation, event handling with propagation control, dynamic positioning, and state management. No backend changes needed.

## Phases

### Phase 1: State Management Setup

Add state variables and utility functions for swap functionality.

**Files:** `src/frontend/js/app.js`

**Changes:**
1. Add `currentWorkoutData` variable to store the workout plan result
2. Add `activeSwapPopup` variable to track open popup
3. Create `getAlternativeExercises(exerciseName)` function:
   - Find exercise in `exercisesCache` by name
   - Get its `sub_region`
   - Filter `exercisesCache` for same `sub_region`, excluding current exercise
   - Return filtered list

### Phase 2: Swap Button Integration

Add swap button to exercise items in workout rendering.

**Files:** `src/frontend/js/app.js`

**Changes:**
1. Modify `renderWorkoutPlan()` to:
   - Store `data` in `currentWorkoutData`
   - Add swap button HTML to exercise item template:
     ```html
     <button class="swap-btn" data-exercise="${ex.name}" title="Switch exercise">⇄</button>
     ```
   - Position button between exercise name and details

2. Add click handler for swap buttons:
   - Use event delegation on workout container
   - Call `stopPropagation()` to prevent modal
   - Call `showSwapPopup(exerciseName, buttonElement)`

### Phase 3: Swap Popup Implementation

Create and manage the swap popup.

**Files:** `src/frontend/js/app.js`, `src/frontend/index.html`

**Changes:**

**HTML (index.html):**
Add popup container before closing body tag:
```html
<div id="swap-popup" class="swap-popup" style="display: none;">
    <div class="swap-popup-header">Switch Exercise</div>
    <div class="swap-popup-list"></div>
</div>
```

**JavaScript (app.js):**

1. Create `showSwapPopup(exerciseName, buttonEl)`:
   - Close any existing popup
   - Get alternatives via `getAlternativeExercises()`
   - Populate `.swap-popup-list` with items
   - Position popup near button (calculate based on button position)
   - Show popup
   - Store reference in `activeSwapPopup`

2. Create `hideSwapPopup()`:
   - Hide popup
   - Clear `activeSwapPopup`

3. Create `positionSwapPopup(buttonEl)`:
   - Get button bounding rect
   - Position popup below button
   - If below viewport, position above button
   - Ensure horizontal containment

4. Add event listeners:
   - Click outside popup → close
   - Escape key → close
   - Click on popup item → swap exercise

### Phase 4: Exercise Swap Logic

Implement the actual swap functionality.

**Files:** `src/frontend/js/app.js`

**Changes:**

1. Create `swapExercise(originalName, newExercise, dayIndex, exerciseIndex)`:
   - Update `currentWorkoutData.workouts[dayIndex].exercises[exerciseIndex]`
   - Copy `sets`, `reps`, `rest_seconds` from original
   - Update `name` to new exercise name
   - Re-render only the affected exercise item (or full workout if simpler)
   - Hide swap popup

2. Modify exercise item template to include indices:
   ```html
   data-day-index="${dayIdx}" data-exercise-index="${exIdx}"
   ```

3. Update click handler to extract indices and pass to `swapExercise()`

### Phase 5: CSS Styling

Add styles for swap button and popup.

**Files:** `src/frontend/css/styles.css`

**Changes:**

```css
/* Swap Button */
.swap-btn {
    background: none;
    border: none;
    font-size: 16px;
    cursor: pointer;
    opacity: 0.4;
    padding: 4px 8px;
    margin-left: auto;
    margin-right: 8px;
    transition: opacity 0.2s;
}

.swap-btn:hover {
    opacity: 0.7;
}

.exercise-item:hover .swap-btn {
    opacity: 0.6;
}

/* Swap Popup */
.swap-popup {
    position: fixed;
    background: var(--surface);
    border-radius: var(--radius);
    box-shadow: var(--shadow-lg);
    min-width: 240px;
    max-width: 320px;
    max-height: 300px;
    overflow-y: auto;
    z-index: 150;
}

.swap-popup-header {
    padding: 12px 16px;
    font-weight: 600;
    border-bottom: 1px solid var(--border);
    color: var(--text);
}

.swap-popup-list {
    padding: 8px 0;
}

.swap-popup-item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 16px;
    cursor: pointer;
    transition: background 0.15s;
}

.swap-popup-item:hover {
    background: var(--background);
}

.swap-popup-item-name {
    flex: 1;
}

.swap-popup-item-meta {
    display: flex;
    gap: 8px;
    align-items: center;
}

.tier-badge {
    font-size: 11px;
    font-weight: 600;
    padding: 2px 6px;
    border-radius: 4px;
    background: var(--primary);
    color: white;
}

.tier-badge.tier-s {
    background: #F59E0B;
}

.tier-badge.tier-a {
    background: var(--primary);
}

.difficulty-tag {
    font-size: 11px;
    color: var(--text-light);
    text-transform: capitalize;
}

.swap-popup-empty {
    padding: 16px;
    text-align: center;
    color: var(--text-light);
}
```

### Phase 6: Integration and Polish

Final integration and edge case handling.

**Files:** `src/frontend/js/app.js`

**Changes:**

1. Update exercise item layout in `renderWorkoutPlan()`:
   - Restructure to: name | swap-btn | details
   - Use flexbox gap for spacing

2. Handle edge cases:
   - No alternatives: Show "No alternatives available" message
   - Exercise not in cache: Don't render swap button for that exercise

3. Add keyboard navigation (optional enhancement):
   - Arrow keys to navigate popup items
   - Enter to select

4. Ensure modal still works correctly:
   - Clicking exercise name/row opens modal
   - Clicking swap button opens popup (not modal)

## Files Summary

| File | Action | Changes |
|------|--------|---------|
| `src/frontend/js/app.js` | Modify | State vars, swap functions, event handlers, updated render |
| `src/frontend/css/styles.css` | Modify | Swap button styles, popup styles, tier badge |
| `src/frontend/index.html` | Modify | Add swap popup container element |

## Data Flow

```
User clicks swap button
        ↓
stopPropagation() (prevent modal)
        ↓
getAlternativeExercises(name)
        ↓
Filter exercisesCache by sub_region
        ↓
showSwapPopup() with alternatives
        ↓
User selects alternative
        ↓
swapExercise() updates currentWorkoutData
        ↓
Re-render affected exercise item
        ↓
hideSwapPopup()
```

## Component Hierarchy

```
#workout-results
└── .workout-days
    └── .day-card
        └── .exercise-list
            └── .exercise-item (click → modal)
                ├── .exercise-name
                ├── .swap-btn (click → popup, stopPropagation)
                └── .exercise-details

#swap-popup (fixed position, shown on demand)
├── .swap-popup-header
└── .swap-popup-list
    └── .swap-popup-item (click → swap)
        ├── .swap-popup-item-name
        └── .swap-popup-item-meta
            ├── .tier-badge
            └── .difficulty-tag
```

## Testing Strategy

### Manual Testing

1. **Swap button visibility**
   - Generate workout plan
   - Verify swap button appears on each exercise
   - Verify button is faded (opacity ~0.4)
   - Verify hover increases opacity

2. **Popup behavior**
   - Click swap button → popup opens
   - Click outside → popup closes
   - Press Escape → popup closes
   - Click another swap button → previous popup closes, new opens

3. **Alternative filtering**
   - Verify alternatives are same sub-region
   - Verify current exercise not in list
   - Verify tier badges display correctly

4. **Swap functionality**
   - Select alternative → exercise updates in UI
   - Click swapped exercise → modal shows new exercise details
   - Sets/reps/rest preserved from original

5. **Edge cases**
   - Exercise with no alternatives → message shown
   - Multiple swaps on same exercise
   - Swap then regenerate workout → fresh data

### Browser Testing

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Mobile viewport (responsive)

## API Contracts

No new API endpoints. Existing endpoint used:

**GET /api/exercises**
```json
{
  "exercises": [
    {
      "id": "incline-barbell-bench-press",
      "name": "Incline Barbell Bench Press",
      "muscle_group": "chest",
      "sub_region": "upper_chest",
      "difficulty": "medium",
      "equipment": ["barbell", "bench", "rack"],
      "type": "compound",
      "nippard_tier": "A",
      "rest": 120
    }
  ]
}
```

Note: The `sub_region` field (returned as `subcategory` via adapter) is critical for filtering alternatives.
