from game.bullet.bullet import Bullet
import config
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from game.game import Game

config = config.Config().bullet

class BulletManager:
    def __init__(self,game:"Game"):
        self._game = game
        self._bullets: List[List[Bullet]] = []
        for _ in range(game.field.rows):
            self._bullets.append([])

    def spawn_bullet(self, row, col):
        self._bullets[row].append(Bullet(self, row, col))

    def get_zombie_hit_by_bullet(self, bullet: "Bullet"):
        return self._game.zombie_manager.get_zombie_hit_by_bullet(bullet)

    def on_tick(self):
        for row in range(self._game.field.rows):
            for bullet in self._bullets[row]:
                bullet.on_tick()
                if not bullet.is_alive:
                    self._bullets[bullet.row].remove(bullet)

    def draw(self, screen):
        for row in range(self._game.field.rows):
            for bullet in self._bullets[row]:
                bullet.draw(screen)