"""Data persistence using JSON Lines format."""

import json
from datetime import datetime
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"


def ensure_data_dir():
    """Create data directory if it doesn't exist."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def append_record(filename, input_data, output_data):
    """Append a record to a JSONL file."""
    ensure_data_dir()
    filepath = DATA_DIR / filename

    record = {
        "timestamp": datetime.now().isoformat(),
        "input": input_data,
        "output": output_data,
    }

    with open(filepath, "a") as f:
        f.write(json.dumps(record) + "\n")


def read_records(filename):
    """Read all records from a JSONL file."""
    filepath = DATA_DIR / filename

    if not filepath.exists():
        return []

    records = []
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))

    return records


def get_stats():
    """Get statistics about collected data."""
    calorie_records = read_records("calorie_calculations.jsonl")
    workout_records = read_records("workout_plans.jsonl")

    return {
        "calorie_calculations": {
            "total": len(calorie_records),
            "last_calculated": calorie_records[-1]["timestamp"] if calorie_records else None,
        },
        "workout_plans": {
            "total": len(workout_records),
            "last_generated": workout_records[-1]["timestamp"] if workout_records else None,
        },
    }


def log_calorie_calculation(input_data, output_data):
    """Log a calorie calculation."""
    append_record("calorie_calculations.jsonl", input_data, output_data)


def log_workout_plan(input_data, output_data):
    """Log a workout plan generation."""
    append_record("workout_plans.jsonl", input_data, output_data)
