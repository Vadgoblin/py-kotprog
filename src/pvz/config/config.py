from types import MappingProxyType
import json
import os
from pathlib import Path
from .validateConfig import validate_config
from importlib.resources import files


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
        config_path = files('pvz').joinpath('config.json')
        if not config_path.is_file():
            raise Exception("config file not found")

        try:
            with config_path.open() as config_file:
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
            "bgm":"bgm.mp3",
            "win_music": "winmusic.ogg",

            "chomp":"chomp.ogg",
            "plant":"plant.ogg",
            "sun_pickup":"points.ogg",
            "splat": "splat.ogg",
            "cherry_bomb" : "cherrybomb.ogg"
        }