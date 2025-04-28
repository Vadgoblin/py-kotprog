from types import MappingProxyType

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
        game = {
            "width": 1080,
            "height": 700,
            "target_fps": 60,
        }
        field = {
            "x":260,
            "y":169,
            "width":730,
            "height":506,
            "rows": 5,
            "columns": 9,
        }
        plant = {
            "width": 80,
            "height": 80,
            "offset_x": 0,
            "offset_y": 10,
            "peashooter":{
                "hp" : 8,
                "sprite" : "assets/peashooter.png",
                "shoot_timeout" : 150 #/ (1000/60),

            },
        }
        bullet = {
            "width": 25,
            "height": 25,
            "sprite": "assets/pea.png",
            "offset_x" : 63,
            "offset_y" : 17,
            "speed" : 3,
        }
        zombie = {
            "width":78,
            "height" : 140,
            "offset_x": 0,
            "offset_y": -40,
            "spawn_x": 1080,
            "sprite": "assets/zombie.png",
        }

        self.plant = MappingProxyType(plant)
        self.zombie = MappingProxyType(zombie)
        self.field = MappingProxyType(field)
        self.bullet = MappingProxyType(bullet)
        self.game = MappingProxyType(game)