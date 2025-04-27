import json

class ConfigManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
        return cls._instance

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self._configs = {
            "window_width" : 1080,
            "window_height" : 700,
            "target_tick_time" : 60,

            "zombie_size" : (78, 140),
            "zombie_sprite" : "assets/zombie.png",
            "zombie_offset_x" : 0,
            "zombie_offset_y" : -40,
            "zombie_spawn_x" : 1080,

            "field_pos": (260, 169),
            "field_size" : (990-260,675-169),
            "field_rows" : 5,
            "field_columns" : 9,
        }

    def get(self, key):
        if key not in self._configs.keys():
            Exception(f"{key} key is not in the config")
        return self._configs[key]