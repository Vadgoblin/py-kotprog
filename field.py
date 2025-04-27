from argparse import ArgumentTypeError

import configManager
import plants.peashooter
from zombie import Zombie

config = configManager.ConfigManager()


def row_to_y(row):
    _, field_height = config.get("field_size")
    _, field_y = config.get("field_pos")
    field_block_height = field_height / config.get("field_rows")
    y = field_y + (row * field_block_height)
    return y

def col_to_x(col):
    field_width, _ = config.get("field_size")
    field_x, _ = config.get("field_pos")
    field_block_width = field_width / config.get("field_columns")
    x = field_x + (col * field_block_width)
    return x


class Field:
    def __init__(self):
        self._rows = config.get("field_rows")
        self._columns = config.get("field_columns")
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
            ArgumentTypeError(f"Expected row to be an integer between 0 and {self._rows - 1}, got {row}")
        self._zombies[row].append(Zombie(row))

    def plant_plant(self, plant_type, row, col):
        if not isinstance(row,int) or row < 0 or row >= self._rows:
            ArgumentTypeError(f"Expected row to be an integer between 0 and {self._rows - 1}, got {row}")
        if not isinstance(col,int) or col < 0 or col >= self._columns:
            ArgumentTypeError(f"Expected row to be an integer between 0 and {self._columns - 1}, got {col}")
        if self._plants[row][col] is not None:
            Exception(f"There is already a plant at row {row} column {col}")

        self._plants[row][col] = plants.peashooter.Peashooter(row, col)




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
            for zombie in self._zombies[row]:
                zombie.on_tick()