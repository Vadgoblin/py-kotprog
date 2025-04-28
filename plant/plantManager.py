import field
from plant.plantFactory import plantFactory
from plant.abstractPlant import AbstractPlant
from typing import TYPE_CHECKING,List, Optional

if TYPE_CHECKING:
    from field import Field
    from zombie import Zombie

class PlantManager:
    def __init__(self, field: 'Field'):
        self._field = field
        self._plants: List[List[AbstractPlant | None]] = []
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
        self._plants[row][col] = plantFactory(self, plant_type, row, col)

    def does_plant_see_zombie(self, plant: "AbstractPlant"):
        return self._field.zombie_manager.does_plant_see_zombie(plant)

    def get_blocking_plant(self, zombie: "Zombie"):
        row = zombie.row
        for col in range(self._field.cols - 1, -1, -1):
            plant = self._plants[row][col]
            if plant is None:
                continue
            plant_x = field.col_to_x(plant.col)
            if zombie.x <= plant_x + plant.width * (4/5) and zombie.x + zombie.width >= plant_x + plant.width / 3:
                return plant
        return None


    def spawn_bullet(self,row, col):
        self._field.bullet_manager.spawn_bullet(row,col)


    def draw(self, screen):
        for row in range(self._field.rows):
            for col in range(self._field.cols):
                plant = self._plants[row][col]
                if plant is not None:
                    plant.draw(screen)

    def on_tick(self):
        for row in range(self._field.rows):
            for col in range(self._field.cols):
                plant = self._plants[row][col]
                if plant is not None:
                    if plant.is_alive:
                        plant.on_tick()
                    else:
                        self._plants[plant.row][plant.col] = None