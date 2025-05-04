import json
import os
import numbers
from config import Config
from game.level.level import Level


def load_level(path):
    _validate_path(path)
    level_data = _load_level_data(path)
    _validate_level_data(level_data)
    level = Level(level_data)
    return level

def _validate_path(path):
    if not os.path.exists(path):
        raise Exception(f"level at {path} not found")
    if not os.path.isfile(path):
        raise Exception(f"{path} is not a file")

def _load_level_data(path):
    with open(path) as file:
        level = json.load(file)
    return level

def _validate_level_data(level_data):
    if not isinstance(level_data,list):
        raise Exception("Invalid level data")

    for entry in level_data:
        _validate_entry(entry)

def _validate_entry(entry):
    _require_type(entry, dict)

    required_keys = ["sleep", "rows"]
    _require_keys(entry,required_keys)

    _validate_sleep(entry)
    _validate_row(entry)

def _validate_sleep(entry):
    _require_type(entry["sleep"], numbers.Number)
    if entry["sleep"] < 0:
        raise Exception("Invalid level data")

def _validate_row(entry):
    _require_type(entry["rows"], list)
    max_rows = Config().field["rows"]
    for row in entry["rows"]:
        _require_type(row, int)
        if not (0 <= row < max_rows):
            raise Exception("Invalid level data")

def _require_keys(_dict, keys):
    for key in keys:
        if key not in _dict:
            raise Exception("Invalid level data")

def _require_type(obj, expected_type):
    if not isinstance(obj, expected_type):
        raise Exception("Invalid level data")