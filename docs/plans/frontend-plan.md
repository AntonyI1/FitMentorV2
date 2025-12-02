# Frontend - Implementation Plan

## Phase 1: HTML Structure

**File:** `src/frontend/index.html`

**Tasks:**
1. Set up document head with meta tags, title, CSS link
2. Create navigation bar with brand
3. Create hero section with headline and CTA buttons
4. Create calorie calculator section:
   - Unit toggle (metric/imperial)
   - Form with all inputs (age, gender, height, weight, activity, goal)
   - Results container (hidden initially)
5. Create workout planner section:
   - Form with all inputs (gender, goal, experience, equipment checkboxes, days)
   - Results container (hidden initially)
6. Create exercise modal (hidden initially)
7. Link JavaScript file

## Phase 2: CSS Styling

**File:** `src/frontend/css/styles.css`

**Tasks:**
1. Define CSS variables (colors, spacing, fonts)
2. Reset and base styles
3. Navigation styles (fixed, gradient background)
4. Hero section (centered, gradient text)
5. Section layout (max-width container, padding)
6. Form styles:
   - Input groups with labels
   - Select dropdowns
   - Checkbox grid for equipment
   - Submit buttons with hover states
7. Unit toggle (pill-style switcher)
8. Results display:
   - Stats cards (BMR, TDEE, Target)
   - Macro cards with colored accents
   - Recommendations list
9. Workout display:
   - Split overview
   - Day cards with exercise lists
   - Exercise items with sets/reps/rest
10. Modal styles (overlay, centered card, close button)
11. Utility classes (loading spinner, error messages)
12. Responsive breakpoints (mobile-first)

## Phase 3: JavaScript Functionality

**File:** `src/frontend/js/app.js`

**Tasks:**
1. Constants (API_URL, DOM selectors)
2. State management (units, exercises cache)
3. Unit conversion functions:
   - lbs ↔ kg
   - ft/in ↔ cm
4. Form value getters with unit conversion
5. API functions:
   - `calculateCalories(data)` - POST to /api/calculate-calories
   - `suggestWorkout(data)` - POST to /api/suggest-workout
   - `fetchExercises()` - GET /api/exercises
6. Render functions:
   - `renderCalorieResults(data)`
   - `renderWorkoutPlan(data)`
   - `renderExerciseModal(exercise)`
7. Event handlers:
   - Unit toggle click
   - Calculator form submit
   - Workout form submit
   - Exercise card click (open modal)
   - Modal close (click outside, X button, Escape key)
8. Form validation (client-side before API call)
9. Loading states (disable button, show spinner)
10. Error handling (display API errors)
11. Initialize on DOMContentLoaded

## Component Hierarchy

```
index.html
├── nav
│   └── brand
├── hero
│   ├── headline
│   ├── subtext
│   └── cta-buttons
├── #calorie-section
│   ├── unit-toggle
│   ├── form#calorie-form
│   │   ├── input[age]
│   │   ├── select[gender]
│   │   ├── input[height] (+ ft/in inputs for imperial)
│   │   ├── input[weight]
│   │   ├── select[activity_level]
│   │   ├── select[goal]
│   │   └── button[submit]
│   └── #calorie-results (hidden)
│       ├── stats-cards
│       ├── macro-cards
│       └── recommendations
├── #workout-section
│   ├── form#workout-form
│   │   ├── select[gender]
│   │   ├── select[goal]
│   │   ├── select[experience]
│   │   ├── checkbox-grid[equipment]
│   │   ├── select[days_per_week]
│   │   └── button[submit]
│   └── #workout-results (hidden)
│       ├── split-overview
│       └── day-cards
│           └── exercise-items (clickable)
└── #exercise-modal (hidden)
    ├── overlay
    └── modal-content
        ├── close-button
        ├── exercise-name
        └── exercise-details
```

## Testing Strategy

1. Manual testing of all form inputs and validation
2. Test unit conversion accuracy
3. Test API integration with running backend
4. Test responsive layout at various breakpoints
5. Test modal open/close behavior
6. Test error states (stop backend, submit form)

## Complexity Estimate

**Medium** - Standard DOM manipulation, no complex state, straightforward API integration.
