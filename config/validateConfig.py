import config
from numbers import Number

_config : "config.Config|None" = None

def validate_config():
    global _config
    _config = config.Config()

    _validate_field()
    _validate_sun()
    _validate_plant()
    _validate_plant_types()
    _validate_bullet()
    _validate_zombie()

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

def _validate_dict(dict_, excepted):
    for key, expected_type in excepted.items():
        if key not in dict_ or not isinstance(dict_[key], expected_type):
            raise Exception(f"error while parsing config")