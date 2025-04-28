import configManager
from managers.plantManager import PlantManager
from managers.zombieManager import ZombieManager

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
        self._cols = config["columns"]
        self._plant_manager = PlantManager(self)
        self._zombie_manager = ZombieManager(self)

    @property
    def rows(self):
        return self._rows

    @property
    def cols(self):
        return self._cols

    @property
    def plant_manager(self):
        return self._plant_manager

    @property
    def zombie_manager(self):
        return self._zombie_manager

    def draw(self, screen):
        self._plant_manager.draw(screen)
        self._zombie_manager.draw(screen)

    def on_tick(self):
        self._plant_manager.on_tick()
        self._zombie_manager.on_tick()