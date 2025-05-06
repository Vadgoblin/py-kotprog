from src.pvz.assets.asset_loader import load_sprite
from src.pvz.config.config import Config
from src.pvz.game import field

config = Config().plant


class GhostPlantManager:
    def __init__(self):
        self._width = config['width']
        self._height = config['height']
        self._offset_x = config['offset_x']
        self._offset_y = config['offset_y']
        self._types = config['types']
        self._load_sprites()

        self._type = None
        self._pos = None

    def _load_sprites(self):
        size = (self._width, self._height)
        sprites = {}
        for _type in self._types:
            path = config[_type]["sprite"]
            sprite = load_sprite(path, size, True)
            sprites[_type] = sprite
        self._sprites = sprites

    def show(self, plant_type, row, col):
        self._type = plant_type
        x = field.col_to_x(col) + self._offset_x
        y = field.row_to_y(row) + self._offset_y
        self._pos = (x, y)

    def hide(self):
        self._type = None

    def draw(self, screen):
        if self._type is not None:
            screen.blit(self._sprites[self._type], self._pos)
