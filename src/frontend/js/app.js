const API_URL = 'http://localhost:5000';

let currentUnit = 'metric';
let exercisesCache = [];

// Store values separately for each unit system
let metricValues = { height: '', weight: '' };
let imperialValues = { heightFt: '', heightIn: '', weight: '' };

// Unit conversion
function lbsToKg(lbs) {
    return lbs / 2.205;
}

function kgToLbs(kg) {
    return kg * 2.205;
}

function ftInToCm(ft, inches) {
    return (ft * 12 + inches) * 2.54;
}

function cmToFtIn(cm) {
    const totalInches = cm / 2.54;
    const ft = Math.floor(totalInches / 12);
    const inches = Math.round(totalInches % 12);
    return { ft, in: inches };
}

// DOM helpers
function $(selector) {
    return document.querySelector(selector);
}

function $$(selector) {
    return document.querySelectorAll(selector);
}

function show(el) {
    if (typeof el === 'string') el = $(el);
    el.style.display = '';
}

function hide(el) {
    if (typeof el === 'string') el = $(el);
    el.style.display = 'none';
}

// API functions
async function calculateCalories(data) {
    const response = await fetch(`${API_URL}/api/calculate-calories`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    const result = await response.json();
    if (!response.ok) throw new Error(result.error || 'Calculation failed');
    return result;
}

async function suggestWorkout(data) {
    const response = await fetch(`${API_URL}/api/suggest-workout`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    const result = await response.json();
    if (!response.ok) throw new Error(result.error || 'Workout generation failed');
    return result;
}

async function fetchExercises() {
    const response = await fetch(`${API_URL}/api/exercises`);
    const result = await response.json();
    if (!response.ok) throw new Error(result.error || 'Failed to fetch exercises');
    return result.exercises;
}

// Render functions
function renderCalorieResults(data) {
    $('#result-bmr').textContent = data.bmr.toLocaleString();
    $('#result-tdee').textContent = data.tdee.toLocaleString();
    $('#result-target').textContent = data.target_calories.toLocaleString();

    $('#macro-protein-grams').textContent = `${data.macros.protein.grams}g`;
    $('#macro-protein-cals').textContent = `${data.macros.protein.calories} kcal`;
    $('#macro-protein-pct').textContent = `${data.macros.protein.percentage}%`;

    $('#macro-carbs-grams').textContent = `${data.macros.carbs.grams}g`;
    $('#macro-carbs-cals').textContent = `${data.macros.carbs.calories} kcal`;
    $('#macro-carbs-pct').textContent = `${data.macros.carbs.percentage}%`;

    $('#macro-fats-grams').textContent = `${data.macros.fats.grams}g`;
    $('#macro-fats-cals').textContent = `${data.macros.fats.calories} kcal`;
    $('#macro-fats-pct').textContent = `${data.macros.fats.percentage}%`;

    const recList = $('#recommendations');
    recList.innerHTML = data.recommendations.map(rec => `<li>${rec}</li>`).join('');

    show('#calorie-results');
    $('#calorie-results').scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function renderWorkoutPlan(data) {
    $('#split-name').textContent = data.split.name;
    $('#progression-method').textContent = data.progression.method;
    $('#progression-details').textContent = `${data.progression.increment} ${data.progression.deload}`;

    const daysContainer = $('#workout-days-list');
    daysContainer.innerHTML = data.workouts.map(workout => `
        <div class="day-card">
            <div class="day-header">
                ${workout.day}
                <span>- ${workout.muscle_groups.join(', ')}</span>
            </div>
            <div class="exercise-list">
                ${workout.exercises.map(ex => `
                    <div class="exercise-item" data-exercise="${ex.name}">
                        <span class="exercise-name">${ex.name}</span>
                        <span class="exercise-details">${ex.sets} x ${ex.reps} | ${ex.rest_seconds}s rest</span>
                    </div>
                `).join('')}
            </div>
        </div>
    `).join('');

    // Add click handlers for exercise items
    $$('.exercise-item').forEach(item => {
        item.addEventListener('click', () => {
            const name = item.dataset.exercise;
            const exercise = exercisesCache.find(e => e.name === name);
            if (exercise) showExerciseModal(exercise);
        });
    });

    show('#workout-results');
    $('#workout-results').scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function showExerciseModal(exercise) {
    $('#modal-exercise-name').textContent = exercise.name;
    $('#modal-muscle-group').textContent = exercise.muscle_group;
    $('#modal-type').textContent = exercise.type;
    $('#modal-difficulty').textContent = exercise.difficulty;
    $('#modal-equipment').textContent = exercise.equipment.join(', ');
    $('#modal-rest').textContent = `${exercise.rest} seconds`;
    show('#exercise-modal');
}

function hideExerciseModal() {
    hide('#exercise-modal');
}

// Form handling
function setLoading(form, loading) {
    const btn = form.querySelector('button[type="submit"]');
    const text = btn.querySelector('.btn-text');
    const spinner = btn.querySelector('.btn-spinner');

    btn.disabled = loading;
    text.style.display = loading ? 'none' : '';
    spinner.style.display = loading ? '' : 'none';
}

function showError(form, message) {
    const errorEl = form.querySelector('.form-error');
    errorEl.textContent = message;
    show(errorEl);
}

function hideError(form) {
    hide(form.querySelector('.form-error'));
}

function getCalorieFormData() {
    const form = $('#calorie-form');
    let height, weight;

    if (currentUnit === 'imperial') {
        const ft = parseInt($('#calc-height-ft').value) || 0;
        const inches = parseInt($('#calc-height-in').value) || 0;
        height = ftInToCm(ft, inches);
        weight = lbsToKg(parseFloat($('#calc-weight').value));
    } else {
        height = parseFloat($('#calc-height').value);
        weight = parseFloat($('#calc-weight').value);
    }

    return {
        age: parseInt($('#calc-age').value),
        gender: $('#calc-gender').value,
        height: Math.round(height * 10) / 10,
        weight: Math.round(weight * 10) / 10,
        activity_level: $('#calc-activity').value,
        goal: $('#calc-goal').value
    };
}

function getWorkoutFormData() {
    const equipment = Array.from($$('input[name="equipment"]:checked')).map(cb => cb.value);

    return {
        gender: $('#workout-gender').value,
        goal: $('#workout-goal').value,
        experience: $('#workout-experience').value,
        equipment: equipment,
        days_per_week: parseInt($('#workout-days-select').value),
        session_duration: 60
    };
}

// Event handlers
function handleUnitToggle(e) {
    const btn = e.target.closest('.unit-btn');
    if (!btn) return;

    const unit = btn.dataset.unit;
    if (unit === currentUnit) return;

    // Update active state
    $$('.unit-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    const heightInput = $('#calc-height');
    const heightFt = $('#calc-height-ft');
    const heightIn = $('#calc-height-in');
    const weightInput = $('#calc-weight');
    const weightLabel = $('#weight-label');

    // Save current values before switching
    if (currentUnit === 'metric') {
        metricValues.height = heightInput.value;
        metricValues.weight = weightInput.value;
    } else {
        imperialValues.heightFt = heightFt.value;
        imperialValues.heightIn = heightIn.value;
        imperialValues.weight = weightInput.value;
    }

    if (unit === 'imperial') {
        // Restore imperial values (empty if never entered)
        heightFt.value = imperialValues.heightFt;
        heightIn.value = imperialValues.heightIn;
        weightInput.value = imperialValues.weight;

        hide('#height-metric');
        show($('.height-imperial'));
        weightLabel.textContent = 'Weight (lbs)';
        weightInput.placeholder = '88-500';
        weightInput.min = 88;
        weightInput.max = 500;
        heightInput.removeAttribute('required');
        heightFt.setAttribute('required', '');
        heightIn.setAttribute('required', '');
    } else {
        // Restore metric values (empty if never entered)
        heightInput.value = metricValues.height;
        weightInput.value = metricValues.weight;

        show('#height-metric');
        hide($('.height-imperial'));
        weightLabel.textContent = 'Weight (kg)';
        weightInput.placeholder = '40-230';
        weightInput.min = 40;
        weightInput.max = 230;
        heightInput.setAttribute('required', '');
        heightFt.removeAttribute('required');
        heightIn.removeAttribute('required');
    }

    currentUnit = unit;
}

async function handleCalorieSubmit(e) {
    e.preventDefault();
    const form = e.target;

    hideError(form);
    setLoading(form, true);

    try {
        const data = getCalorieFormData();
        const result = await calculateCalories(data);
        renderCalorieResults(result);
    } catch (err) {
        showError(form, err.message || 'Cannot connect to server. Make sure the backend is running.');
    } finally {
        setLoading(form, false);
    }
}

async function handleWorkoutSubmit(e) {
    e.preventDefault();
    const form = e.target;

    hideError(form);
    setLoading(form, true);

    try {
        const data = getWorkoutFormData();
        if (data.equipment.length === 0) {
            throw new Error('Please select at least one equipment option');
        }
        const result = await suggestWorkout(data);
        renderWorkoutPlan(result);
    } catch (err) {
        showError(form, err.message || 'Cannot connect to server. Make sure the backend is running.');
    } finally {
        setLoading(form, false);
    }
}

// Initialize
document.addEventListener('DOMContentLoaded', async () => {
    // Load exercises for modal
    try {
        exercisesCache = await fetchExercises();
    } catch (err) {
        console.warn('Could not load exercises:', err.message);
    }

    // Unit toggle
    $('.unit-toggle').addEventListener('click', handleUnitToggle);

    // Forms
    $('#calorie-form').addEventListener('submit', handleCalorieSubmit);
    $('#workout-form').addEventListener('submit', handleWorkoutSubmit);

    // Modal
    $('.modal-overlay').addEventListener('click', hideExerciseModal);
    $('.modal-close').addEventListener('click', hideExerciseModal);
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') hideExerciseModal();
    });
});
