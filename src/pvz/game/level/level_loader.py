import json
import numbers
from importlib.resources import files

from src.pvz.config import Config
from src.pvz.game.level.level import Level


def load_level(name):
    level_file = _resolve_level_path(name)
    level_data = _load_level_data(level_file)
    _validate_level_data(level_data)
    level = Level(level_data)
    return level


def _resolve_level_path(name: str):
    return files('pvz').joinpath("levels", f"{name}.json")


def _load_level_data(level_file):
    with level_file.open() as file:
        level = json.load(file)
    return level


def _validate_level_data(level_data):
    if not isinstance(level_data, list):
        raise Exception("Invalid level data")

    for entry in level_data:
        _validate_entry(entry)


def _validate_entry(entry):
    _require_type(entry, dict)

    required_keys = ["sleep", "rows"]
    _require_keys(entry, required_keys)

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
