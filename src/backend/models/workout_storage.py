"""Workout save/load functionality using JSON Lines format."""

import json
import re
from datetime import datetime
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"
SAVED_WORKOUTS_FILE = "saved_workouts.jsonl"


def ensure_data_dir():
    """Create data directory if it doesn't exist."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def normalize_name(name):
    """Normalize a workout name for storage and lookup.

    - Strips whitespace
    - Converts to lowercase
    - Removes characters that aren't alphanumeric, space, or hyphen
    """
    if not name:
        return ""

    # Strip and lowercase
    normalized = name.strip().lower()

    # Remove any character that isn't alphanumeric, space, or hyphen
    normalized = re.sub(r"[^a-z0-9\s\-]", "", normalized)

    # Collapse multiple spaces into one
    normalized = re.sub(r"\s+", " ", normalized)

    return normalized.strip()


def validate_name(name):
    """Validate a workout name.

    Returns (is_valid, error_message).
    """
    if not name:
        return False, "Name is required"

    normalized = normalize_name(name)

    if len(normalized) < 3:
        return False, "Name must be at least 3 characters"

    if len(normalized) > 30:
        return False, "Name must be 30 characters or less"

    return True, ""


def _read_all_records():
    """Read all records from the JSONL file."""
    filepath = DATA_DIR / SAVED_WORKOUTS_FILE

    if not filepath.exists():
        return []

    records = []
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError:
                    continue

    return records


def _write_all_records(records):
    """Write all records to the JSONL file."""
    ensure_data_dir()
    filepath = DATA_DIR / SAVED_WORKOUTS_FILE

    with open(filepath, "w") as f:
        for record in records:
            f.write(json.dumps(record) + "\n")


def save_workout(name, workout, input_params):
    """Save a workout with the given name.

    Returns a dict with success status and metadata.
    """
    is_valid, error = validate_name(name)
    if not is_valid:
        return {"success": False, "error": error}

    normalized = normalize_name(name)
    now = datetime.now().isoformat()

    # Read existing records
    records = _read_all_records()

    # Check if name exists
    existing_index = None
    for i, record in enumerate(records):
        if record.get("name") == normalized:
            existing_index = i
            break

    new_record = {
        "name": normalized,
        "saved_at": now,
        "input_params": input_params,
        "workout": workout,
    }

    overwritten = existing_index is not None

    if overwritten:
        records[existing_index] = new_record
    else:
        records.append(new_record)

    _write_all_records(records)

    message = "Workout updated successfully" if overwritten else "Workout saved successfully"

    return {
        "success": True,
        "name": normalized,
        "message": message,
        "overwritten": overwritten,
    }


def load_workout(name):
    """Load a workout by name.

    Returns the workout record or None if not found.
    """
    if not name:
        return None

    normalized = normalize_name(name)
    records = _read_all_records()

    for record in records:
        if record.get("name") == normalized:
            return {
                "success": True,
                "name": record["name"],
                "workout": record["workout"],
                "input_params": record["input_params"],
                "saved_at": record["saved_at"],
            }

    return None


def workout_exists(name):
    """Check if a workout with the given name exists.

    Returns a dict with exists status and saved_at timestamp.
    """
    if not name:
        return {"exists": False, "saved_at": None}

    normalized = normalize_name(name)
    records = _read_all_records()

    for record in records:
        if record.get("name") == normalized:
            return {"exists": True, "saved_at": record.get("saved_at")}

    return {"exists": False, "saved_at": None}
