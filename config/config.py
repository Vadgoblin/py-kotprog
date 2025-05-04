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
        except:
            raise Exception("error occurred while parsing config")

        validate_config()

        self.menu = {
            "background" : "assets/menu.png",
            "exit_button_edges": ((921, 556), (1032, 556), (1032, 672), (921, 672)),
            "easy_button_edges" : ((538, 105),(973, 148),(937, 317),(523, 260)),
            "normal_button_edges" : ((530, 266), (938, 334),(910, 439),(533, 369)),
            "hard_button_edges" : ((542, 381), (902, 447), (880, 549), (541, 478)),
        }