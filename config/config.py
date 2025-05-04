from types import MappingProxyType
import json
import os
from .validateConfig import validate_config

CONFIG_PATH = "config.json"

class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            Config._init(cls._instance)
        return cls._instance

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def _init(self):
        if not os.path.exists(CONFIG_PATH):
            raise Exception("config file not found")

        try:
            with open(CONFIG_PATH) as config_file:
                config = json.load(config_file)
                self.plant = MappingProxyType(config["plant"])
                self.zombie = MappingProxyType(config["zombie"])
                self.field = MappingProxyType(config["field"])
                self.bullet = MappingProxyType(config["bullet"])
                self.game = MappingProxyType(config["game"])
                self.sun = MappingProxyType(config["sun"])
                self.menu = MappingProxyType(config["menu"])
        except:
            raise Exception("error occurred while parsing config")

        validate_config()

        self.audio = {
            "num_of_channels":1000,
            "bgm":"assets/bgm.mp3",
            "win_music": "assets/winmusic.ogg",

            "chomp":"assets/chomp.ogg",
            "plant":"assets/plant.ogg",
            "sun_pickup":"assets/points.ogg",
            "splat": "assets/splat.ogg",
            "cherry_bomb" : "assets/cherrybomb.ogg"
        }