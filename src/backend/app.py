"""FitMentor V2 Backend - Flask API Server."""

from flask import Flask, request, jsonify

from models import calorie_calculator, workout_suggester, data_collector
from models.exercises import get_all_exercises

app = Flask(__name__)


@app.after_request
def add_cors_headers(response):
    """Add CORS headers to all responses."""
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response

VERSION = "2.0.0"


@app.route("/")
def index():
    """Return API info and version."""
    return jsonify({
        "name": "FitMentor API",
        "version": VERSION,
        "endpoints": [
            {"method": "GET", "path": "/", "description": "API info"},
            {"method": "POST", "path": "/api/calculate-calories", "description": "Calculate calories and macros"},
            {"method": "POST", "path": "/api/suggest-workout", "description": "Generate workout plan"},
            {"method": "GET", "path": "/api/exercises", "description": "Get exercise database"},
            {"method": "GET", "path": "/api/stats", "description": "Get data collection stats"},
        ],
    })


@app.route("/api/calculate-calories", methods=["POST"])
def calculate_calories():
    """Calculate calories and macronutrients."""
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()

    try:
        result = calorie_calculator.calculate(data)
        data_collector.log_calorie_calculation(data, result)
        return jsonify(result)
    except calorie_calculator.ValidationError as e:
        return jsonify({"error": str(e)}), 400


@app.route("/api/suggest-workout", methods=["POST"])
def suggest_workout():
    """Generate a workout plan."""
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()

    try:
        result = workout_suggester.suggest(data)
        data_collector.log_workout_plan(data, result)
        return jsonify(result)
    except workout_suggester.ValidationError as e:
        return jsonify({"error": str(e)}), 400


@app.route("/api/exercises", methods=["GET"])
def get_exercises():
    """Return the complete exercise database."""
    exercises = get_all_exercises()
    return jsonify({
        "count": len(exercises),
        "exercises": exercises,
    })


@app.route("/api/stats", methods=["GET"])
def get_stats():
    """Return data collection statistics."""
    stats = data_collector.get_stats()
    return jsonify(stats)


@app.errorhandler(400)
def bad_request(e):
    """Handle 400 errors."""
    return jsonify({"error": "Bad request"}), 400


@app.errorhandler(404)
def not_found(e):
    """Handle 404 errors."""
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors."""
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
