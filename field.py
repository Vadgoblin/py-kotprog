from argparse import ArgumentTypeError

import configManager
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

    def spawn_zombie(self, row):
        if not isinstance(row,int) or row < 0 or row >= self._rows:
            ArgumentTypeError(f"Expected row to be an integer between 0 and {self._rows - 1}, got {row}")
        self._zombies[row].append(Zombie(row))


    def draw(self, screen):
        for row in range(self._rows):
            for zombie in self._zombies[row]:
                zombie.draw(screen)

    def onTick(self):
        for row in range(self._rows):
            for zombie in self._zombies[row]:
                zombie.onTick()