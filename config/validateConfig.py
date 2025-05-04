from typing import List

import config
from numbers import Number

_config : "config.Config|None" = None

def validate_config():
    try:
        global _config
        _config = config.Config()

        _validate_field()
        _validate_sun()
        _validate_plant()
        _validate_plant_types()
        _validate_bullet()
        _validate_zombie()
        _validate_menu()
    except:
        _rise_exception()

def _validate_game():
    game = _config.game
    expected_game = {
        "width": Number,
        "height": Number,
        "target_fps": Number,
        "font": str,
        "background": str
    }
    _validate_dict(game, expected_game)

def _validate_field():
    field = _config.field
    expected_field = {
        "x": Number,
        "y": Number,
        "width": Number,
        "height": Number,
        "rows": Number,
        "columns": Number
    }
    _validate_dict(field, expected_field)

def _validate_sun():
    sun = _config.sun
    expected_sun = {
        "sprite": str,
        "width": Number,
        "height": Number,
        "lifespan": Number,
        "collect_speed": Number,
        "sky_fall_speed": Number,
        "sky_fall_interval_min": Number,
        "sky_fall_interval_max": Number,
        "sunflower_max_random_distance": Number
    }
    _validate_dict(sun,expected_sun)

def _validate_plant():
    plant = _config.plant
    expected_plant = {
        "width": Number,
        "height": Number,
        "offset_x": Number,
        "offset_y": Number,
        "types": list
    }
    _validate_dict(plant,expected_plant)

def _validate_plant_types():
    plant = _config.plant
    expected_plant_types = {
        "peashooter": {
            "hp": Number,
            "sprite": str,
            "shoot_timeout": Number,
            "cost": Number,
            "recharge_time": Number
        },
        "sunflower": {
            "hp": Number,
            "sprite": str,
            "cost": Number,
            "recharge_time": Number,
            "sun_spawn_interval": Number
        },
        "wallnut": {
            "hp": Number,
            "cost": Number,
            "recharge_time": Number,
            "sprite": str
        },
        "cherrybomb": {
            "hp": Number,
            "cost": Number,
            "recharge_time": Number,
            "sprite": str,
            "explode_time": Number,
            "damage": Number
        }
    }
    for plant_name, expected_fields in expected_plant_types.items():
        if plant_name not in plant:
            raise Exception(f"error while parsing config")
        for key, expected_type in expected_fields.items():
            if key not in plant[plant_name]:
                raise Exception(f"error while parsing config")
            elif not isinstance(plant[plant_name][key], expected_type):
                raise Exception(f"error while parsing config")

def _validate_bullet():
    bullet = _config.bullet
    expected_bullet = {
        "width": Number,
        "height": Number,
        "sprite": str,
        "offset_x": Number,
        "offset_y": Number,
        "speed": Number
    }
    _validate_dict(bullet,expected_bullet)

def _validate_zombie():
    zombie = _config.zombie
    expected_zombie = {
        "width": Number,
        "height": Number,
        "offset_x": Number,
        "offset_y": Number,
        "spawn_x": Number,
        "defeat_x": Number,
        "sprite": str,
        "eat_timeout": Number,
        "hp": Number
    }
    _validate_dict(zombie,expected_zombie)

def _validate_menu():
    menu = _config.menu
    expected_menu = {
        "background": str,
        "exit_button_edges": List,
        "easy_button_edges": List,
        "normal_button_edges": List,
        "hard_button_edges": List,
    }
    _validate_dict(menu,expected_menu)

    def is_coord_pair(pair):
        return (isinstance(pair, list) and len(pair) == 2 and
                all(isinstance(p, Number) for p in pair))

    def is_quad_edge_list(edge_list):
        return (isinstance(edge_list, list) and len(edge_list) == 4 and
                all(is_coord_pair(p) for p in edge_list))

    for edge_key in ["exit_button_edges", "easy_button_edges", "normal_button_edges", "hard_button_edges"]:
        if edge_key in menu and not is_quad_edge_list(menu[edge_key]):
            _rise_exception()


def _validate_dict(dict_, excepted):
    for key, expected_type in excepted.items():
        if key not in dict_ or not isinstance(dict_[key], expected_type):
            _rise_exception()

def _rise_exception():
    raise Exception(f"invalid config")