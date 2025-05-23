from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from src.pvz.config.config import Config
from src.pvz.game import field

if TYPE_CHECKING:
    from src.pvz.game.plant.plant_manager import PlantManager

config = Config().plant


class AbstractPlant(ABC):
    def __init__(self, plant_manager: "PlantManager", row, col, hp):
        self._plant_manager = plant_manager
        self._row = row
        self._col = col
        self._hp = hp
        self._sprite = None
        self._width = config["width"]
        self._offset_x = config["offset_x"]
        self._offset_y = config["offset_y"]

    @property
    def is_alive(self):
        return self._hp > 0

    @property
    def width(self):
        return self._width

    @abstractmethod
    def on_tick(self):
        pass

    def draw(self, screen):
        x = field.col_to_x(self._col) + self._offset_x
        y = field.row_to_y(self._row) + self._offset_y
        screen.blit(self._sprite, (x, y))

    def suffer_damage(self):
        self._hp -= 1

    @property
    def row(self):
        return self._row

    @property
    def col(self):
        return self._col
