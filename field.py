import configManager
import plants.plantFactory
from zombie import Zombie

config = configManager.ConfigManager().field


def row_to_y(row):
    field_height = config["height"]
    field_y = config["y"]
    field_block_height = field_height / config["rows"]
    y = field_y + (row * field_block_height)
    return y

def col_to_x(col):
    field_width = config["height"]
    field_x = config["x"]
    field_block_width = field_width / config["columns"]
    x = field_x + (col * field_block_width)
    return x


class Field:
    def __init__(self):
        self._rows = config["rows"]
        self._columns = config["columns"]
        self._zombies = []
        for _ in range(self._rows):
            self._zombies.append([])

        self._plants = []
        for row in range(self._rows):
            self._plants.append([])
            for _ in range(self._columns):
                self._plants[row].append(None)

    def spawn_zombie(self, row):
        if not isinstance(row,int) or row < 0 or row >= self._rows:
            raise Exception(f"Expected row to be an integer between 0 and {self._rows - 1}, got {row}")
        self._zombies[row].append(Zombie(row))

    def plant_plant(self, plant_type, row, col):
        if not isinstance(row,int) or row < 0 or row >= self._rows:
            raise Exception(f"Expected row to be an integer between 0 and {self._rows - 1}, got {row}")
        if not isinstance(col,int) or col < 0 or col >= self._columns:
            raise Exception(f"Expected row to be an integer between 0 and {self._columns - 1}, got {col}")
        if self._plants[row][col] is not None:
            raise Exception(f"There is already a plant at row {row} column {col}")

        self._plants[row][col] = plants.plantFactory.plantFactory(plant_type, row, col)




    def draw(self, screen):
        for row in range(self._rows):
            for col in range(self._columns):
                plant = self._plants[row][col]
                if plant is not None:
                    plant.draw(screen)
        for row in range(self._rows):
            for zombie in self._zombies[row]:
                zombie.draw(screen)

    def on_tick(self):
        for row in range(self._rows):
            for col in range(self._columns):
                plant = self._plants[row][col]
                if plant is not None:
                    plant.on_tick()
        for row in range(self._rows):
            for zombie in self._zombies[row]:
                zombie.on_tick()
                