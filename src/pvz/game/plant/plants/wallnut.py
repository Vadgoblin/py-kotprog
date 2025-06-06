from typing import TYPE_CHECKING

from src.pvz.assets.asset_loader import load_sprite
from src.pvz.config.config import Config
from src.pvz.game.plant.plants.abstract_plant import AbstractPlant

if TYPE_CHECKING:
    from src.pvz.game.plant.plant_manager import PlantManager

config = Config().plant


def _get_sprite():
    sprite_path = config["wallnut"]["sprite"]
    width = config["width"]
    height = config["height"]
    return load_sprite(sprite_path, (width, height))


class Wallnut(AbstractPlant):
    def __init__(self, plant_manager: "PlantManager", row, col):
        hp = config["wallnut"]["hp"]
        super().__init__(plant_manager, row, col, hp)
        self._sprite = _get_sprite()

    def on_tick(self):
        pass
