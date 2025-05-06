from typing import TYPE_CHECKING

from src.pvz.assets.asset_loader import load_sprite
from src.pvz.config.config import Config
from src.pvz.game import sound_player, field

if TYPE_CHECKING:
    from src.pvz.game.bullet.bullet_manager import BulletManager
    from pygame.surface import Surface

config = Config().bullet


class Bullet:
    def __init__(self, bullet_manager: "BulletManager", row, col):
        self._bullet_manager = bullet_manager
        self._row = row
        self._x = field.col_to_x(col) + config["offset_x"]
        self._y = field.row_to_y(row) + config["offset_y"]
        self._width = config["width"]
        self._height = config["height"]
        self._sprite = load_sprite(config["sprite"], (self._width, self._height))
        self._despawn_x = Config().game["width"]
        self._is_alive = True

    @property
    def row(self):
        return self._row

    @property
    def x(self):
        return self._x

    @property
    def width(self):
        return self._width

    @property
    def is_alive(self):
        if not self._is_alive:
            return False
        if self.x > self._despawn_x:
            return False
        return True

    def on_tick(self):
        hit_zombie = self._bullet_manager.get_zombie_hit_by_bullet(self)
        if hit_zombie is None:
            self._x += config["speed"]
        else:
            sound_player.play_splat()
            hit_zombie.suffer_damage()
            self._is_alive = False

    def draw(self, screen: "Surface"):
        screen.blit(self._sprite, (self._x, self._y))
