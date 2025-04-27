from plants.plantFactory import plantFactory
from plants.abstractPlant import AbstractPlant
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from field import Field

class PlantManager:
    def __init__(self, field: 'Field'):
        self._field = field
        self._plants = []
        for row in range(self._field.rows):
            self._plants.append([])
            for _ in range(self._field.cols):
                self._plants[row].append(None)

    def plant_plant(self, plant_type, row, col):
        if not isinstance(row,int) or row < 0 or row >= self._field.rows:
            raise Exception(f"Expected row to be an integer between 0 and {self._field.rows- 1}, got {row}")
        if not isinstance(col,int) or col < 0 or col >= self._field.cols:
            raise Exception(f"Expected row to be an integer between 0 and {self._field.cols - 1}, got {col}")
        if self._plants[row][col] is not None:
            raise Exception(f"There is already a plant at row {row} column {col}")
        self._plants[row][col] = plantFactory(plant_type, row, col)

    def draw(self, screen):
        self._iterate_plants(AbstractPlant.draw, screen)

    def on_tick(self):
        self._iterate_plants(AbstractPlant.on_tick)

    def _iterate_plants(self, action, *args):
        for row in range(self._field.rows):
            for col in range(self._field.cols):
                plant = self._plants[row][col]
                if plant is not None:
                    action(plant, *args)