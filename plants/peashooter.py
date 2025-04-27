import configManager
import spriteLoader
from plants.abstractPlant import AbstractPlant

class Peashooter(AbstractPlant):
    def __init__(self,row, col):
        hp =  configManager.ConfigManager().get("peashooter_hp")
        super().__init__(row,col,hp)
        self.shoot_timeout = 0
        self._sprite = self._get_sprite()

    def _get_sprite(self):
        config = configManager.ConfigManager()
        sprite_path = config.get("peashooter_sprite")
        width = config.get("plant_width")
        height = config.get("plant_height")
        return spriteLoader.load(sprite_path,(width,height))

    def on_tick(self):
        if self.shoot_timeout == 0:
            pass