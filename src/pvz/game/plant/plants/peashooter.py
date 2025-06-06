from typing import TYPE_CHECKING

from src.pvz.assets.asset_loader import load_sprite
from src.pvz.config.config import Config
from src.pvz.game.plant.plants.abstract_plant import AbstractPlant

if TYPE_CHECKING:
    from src.pvz.game.plant.plant_manager import PlantManager

config = Config().plant


def _get_sprite():
    sprite_path = config["peashooter"]["sprite"]
    width = config["width"]
    height = config["height"]
    return load_sprite(sprite_path, (width, height))


class Peashooter(AbstractPlant):
    def __init__(self, plant_manager: "PlantManager", row, col):
        hp = config["peashooter"]["hp"]
        super().__init__(plant_manager, row, col, hp)
        self.shoot_timeout = 0
        self._sprite = _get_sprite()

    def on_tick(self):
        if self.shoot_timeout > 0:
            self.shoot_timeout -= 1
            return
        if self._plant_manager.does_plant_see_zombie(self):
            self._plant_manager.spawn_bullet(self.row, self.col)
            self.shoot_timeout = config["peashooter"]["shoot_timeout"]
