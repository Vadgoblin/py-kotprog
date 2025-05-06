import json
from importlib.resources import files
from types import MappingProxyType

from .validate_config import validate_config


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
                self.audio = MappingProxyType(config["audio"])
        except:
            raise Exception("error occurred while parsing config")

        validate_config()
