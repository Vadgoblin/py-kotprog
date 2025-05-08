from numbers import Number
from typing import List

from src.pvz import config
from .invalid_config_error import InvalidConfigError


def validate_config():
    _config = config.Config()

    _validate_game(_config)
    _validate_field(_config)
    _validate_sun(_config)
    _validate_plant(_config)
    _validate_plant_types(_config)
    _validate_bullet(_config)
    _validate_zombie(_config)
    _validate_audio(_config)
    _validate_menu(_config)


def _validate_game(_config):
    game = _config.game
    expected_game = {
        "width": Number,
        "height": Number,
        "target_fps": Number,
        "text_font": str,
        "number_font": str,
        "background": str
    }
    _validate_dict(game, expected_game)


def _validate_field(_config):
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


def _validate_sun(_config):
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
    _validate_dict(sun, expected_sun)


def _validate_plant(_config):
    plant = _config.plant
    expected_plant = {
        "width": Number,
        "height": Number,
        "offset_x": Number,
        "offset_y": Number,
        "types": list
    }
    _validate_dict(plant, expected_plant)


def _validate_plant_types(_config):
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
            raise InvalidConfigError()
        for key, expected_type in expected_fields.items():
            if key not in plant[plant_name]:
                raise InvalidConfigError()
            if not isinstance(plant[plant_name][key], expected_type):
                raise InvalidConfigError()


def _validate_bullet(_config):
    bullet = _config.bullet
    expected_bullet = {
        "width": Number,
        "height": Number,
        "sprite": str,
        "offset_x": Number,
        "offset_y": Number,
        "speed": Number
    }
    _validate_dict(bullet, expected_bullet)


def _validate_zombie(_config):
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
    _validate_dict(zombie, expected_zombie)


def _validate_audio(_config):
    audio = _config.audio
    expected_audio = {
        "num_of_channels": int,
        "bgm": str,
        "win_music": str,
        "chomp": str,
        "plant": str,
        "sun_pickup": str,
        "splat": str,
        "cherry_bomb": str,
    }
    _validate_dict(audio, expected_audio)


def _validate_menu(_config):
    menu = _config.menu
    expected_menu = {
        "background": str,
        "exit_button_edges": List,
        "easy_button_edges": List,
        "normal_button_edges": List,
        "hard_button_edges": List,
    }
    _validate_dict(menu, expected_menu)

    def is_coord_pair(pair):
        return (isinstance(pair, list) and len(pair) == 2 and
                all(isinstance(p, Number) for p in pair))

    def is_quad_edge_list(edge_list):
        return (isinstance(edge_list, list) and len(edge_list) == 4 and
                all(is_coord_pair(p) for p in edge_list))

    for edge_key in ["exit_button_edges", "easy_button_edges",
                     "normal_button_edges", "hard_button_edges"]:
        if edge_key in menu and not is_quad_edge_list(menu[edge_key]):
            raise InvalidConfigError()


def _validate_dict(dict_, excepted):
    for key, expected_type in excepted.items():
        if key not in dict_ or not isinstance(dict_[key], expected_type):
            raise InvalidConfigError()
