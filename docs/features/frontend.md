# Frontend

## Overview

Single-page web application providing the user interface for FitMentor's calorie calculator and workout planner. Built with vanilla HTML, CSS, and JavaScript, connecting to the Flask backend API.

## User Stories

- As a user, I can calculate my daily calorie and macro targets by entering my stats
- As a user, I can toggle between metric and imperial units
- As a user, I can generate a personalized workout plan based on my goals and equipment
- As a user, I can view exercise details including muscle groups and equipment needed
- As a user, I can navigate easily between the calculator and workout planner

## Acceptance Criteria

- [x] Page loads and displays hero section with CTAs
- [x] Calorie calculator form validates all inputs before submission
- [x] Unit toggle switches between metric (kg/cm) and imperial (lbs/ft-in)
- [x] Calculator displays BMR, TDEE, target calories, and macro breakdown
- [x] Macro cards show grams, calories, and percentages
- [x] Workout planner form accepts all required inputs
- [x] Equipment selection allows multiple choices
- [x] Workout plan displays split, daily exercises, sets/reps/rest
- [x] Exercise cards are clickable to show details in modal
- [x] All API errors display user-friendly messages
- [x] Responsive design works on mobile and desktop

## Technical Requirements

### Files

| File | Purpose |
|------|---------|
| `index.html` | Page structure and sections |
| `css/styles.css` | All styling with CSS variables |
| `js/app.js` | API calls, form handling, DOM manipulation |

### Sections

1. **Navigation** - Fixed navbar with brand logo
2. **Hero** - Headline, subtext, CTA buttons
3. **Calorie Calculator** - Unit toggle, input form, results display
4. **Workout Planner** - Input form, plan display
5. **Exercise Modal** - Overlay with exercise details

### API Integration

| Endpoint | Trigger |
|----------|---------|
| POST `/api/calculate-calories` | Calculator form submit |
| POST `/api/suggest-workout` | Workout form submit |
| GET `/api/exercises` | Page load (cache for modal) |

### Design System

| Token | Value |
|-------|-------|
| Primary | #6366F1 (Indigo) |
| Primary Gradient | #6366F1 → #8B5CF6 |
| Accent | #F59E0B (Amber) |
| Success | #10B981 (Emerald) |
| Background | #F8FAFC |
| Text | #1E293B |
| Font | System font stack |

## Dependencies

- Backend API running on port 5000
- No external libraries (vanilla JS only)

## Edge Cases and Error States

| Scenario | Handling |
|----------|----------|
| API unreachable | Show "Cannot connect to server" message |
| Validation error from API | Display error message near form |
| Empty workout plan | Show message suggesting different equipment |
| Form submitted while loading | Disable submit button, show spinner |
| Invalid number input | Prevent non-numeric characters |
| Unit conversion | Convert values when toggling units |
