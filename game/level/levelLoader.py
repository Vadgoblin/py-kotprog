import json
import os
import numbers
from config import Config
from game.level.level import Level


def load_level(path):
    _validate_path(path)
    level_data = _load_level_data(path)
    print(level_data)
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
        if not isinstance(entry,dict):
            raise Exception("Invalid level data")
        if "sleep" not in entry.keys():
            raise Exception("Invalid level data")
        if "rows" not in entry.keys():
            raise Exception("Invalid level data")
        if not isinstance(entry["sleep"], numbers.Number):
            raise Exception("Invalid level data")
        if entry["sleep"] < 0:
            raise Exception("Invalid level data")
        if not isinstance(entry["rows"],list):
            raise Exception("Invalid level data")

        for _row in entry["rows"]:
            if not isinstance(_row,int):
                raise Exception("Invalid level data")
            if _row < 0 or _row >= Config().field["rows"]:
                raise Exception("Invalid level data")