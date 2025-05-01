from types import MappingProxyType

class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
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
            "font": "assets/font.ttf",
            "background": "assets/background.png",
        }
        field = {
            "x":260,
            "y":169,
            "width":730,
            "height":506,
            "rows": 5,
            "columns": 9,
        }
        sun = {
            "sprite": "assets/sun.png",
            "width": 78,
            "height": 78,
            "lifespan" : 13000/16,
            "collect_speed": 20,
            "sky_fall_speed": 1,
            "sky_fall_interval_min": 5000 / 16,
            "sky_fall_interval_max": 17000 / 16,
            "sunflower_max_random_distance" : 25
        }
        plant = {
            "width": 80,
            "height": 80,
            "offset_x": 0,
            "offset_y": 10,
            "types": ["peashooter","sunflower","wallnut","cherrybomb"],
            "peashooter":{
                "hp" : 8,
                "sprite" : "assets/peashooter.png",
                "shoot_timeout" : 150,
                "cost" : 100,
                "recharge_time" : 7500 /16
            },
            "sunflower":{
                "hp": 8,
                "sprite": "assets/sunflower.png",
                "cost": 50,
                "recharge_time": 7500 / 16,
                "sun_spawn_interval" : 14000/16
            },
            "wallnut":{
                "hp":72,
                "cost" : 50,
                "recharge_time": 30000 / 16,
                "sprite" : "assets/wallnut.png",
            },
            "cherrybomb":{
                "hp":float("inf"),
                "cost":15,
                "recharge_time": 50000 / 16,
                "sprite": "assets/cherrybomb.png",
                "explode_time": 1000 / 16,
                "damage": 9999
            }
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
            "eat_timeout": 500/(1000/60),
            "hp": 10,
        }

        self.plant = MappingProxyType(plant)
        self.zombie = MappingProxyType(zombie)
        self.field = MappingProxyType(field)
        self.bullet = MappingProxyType(bullet)
        self.game = MappingProxyType(game)
        self.sun = MappingProxyType(sun)