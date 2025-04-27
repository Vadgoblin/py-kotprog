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
            "windowWidth" : 1080,
            "windowHeight" : 700,
        }

    def get(self, key):
        if key not in self._configs.keys():
            Exception(f"{key} key is not in the config")
        return self._configs[key]