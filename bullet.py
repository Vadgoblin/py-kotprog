import field
import spriteLoader
import configManager

config = configManager.ConfigManager().bullet

class Bullet:
    def __init__(self, row, col):
        self._x = field.col_to_x(col) + config["offset_x"]
        self._y = field.row_to_y(row) + config["offset_y"]
        self._width = config["width"]
        self._height = config["height"]
        self._sprite = spriteLoader.load(config["sprite"], (self._width, self._height))

    def on_tick(self):
        self._x += config["speed"]

    def draw(self, screen):
        screen.blit(self._sprite, (self._x, self._y))
        pass