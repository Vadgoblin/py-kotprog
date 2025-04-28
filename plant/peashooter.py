from config import Config
import spriteLoader
from plant.abstractPlant import AbstractPlant
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plant.plantManager import PlantManager


config = Config().plant

class Peashooter(AbstractPlant):
    def __init__(self,plant_manager : "PlantManager", row, col):
        hp =  config["peashooter"]["hp"]
        super().__init__(plant_manager, row,col,hp)
        self.shoot_timeout = 0
        self._sprite = self._get_sprite()

    def _get_sprite(self):
        sprite_path = config["peashooter"]["sprite"]
        width = config["width"]
        height = config["height"]
        return spriteLoader.load(sprite_path,(width,height))

    def on_tick(self):
        if self.shoot_timeout > 0:
            self.shoot_timeout -= 1
            return
        if self._plant_manager.does_plant_see_zombie(self):
            self._plant_manager.spawn_bullet(self.row, self.col)
            self.shoot_timeout = config["peashooter"]["shoot_timeout"]