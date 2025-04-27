import configManager
import spriteLoader
from plants.abstractPlant import AbstractPlant

config = configManager.ConfigManager().plant

class Peashooter(AbstractPlant):
    def __init__(self,row, col):
        hp =  config["peashooter"]["hp"]
        super().__init__(row,col,hp)
        self.shoot_timeout = 0
        self._sprite = self._get_sprite()

    def _get_sprite(self):
        sprite_path = config["peashooter"]["sprite"]
        width = config["width"]
        height = config["height"]
        return spriteLoader.load(sprite_path,(width,height))

    def on_tick(self):
        if self.shoot_timeout == 0:
            pass