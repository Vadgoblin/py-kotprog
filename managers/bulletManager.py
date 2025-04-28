from bullet import Bullet
import configManager
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from field import Field

config = configManager.ConfigManager().bullet

class BulletManager:
    def __init__(self,field:"Field"):
        self._field = field
        self._bullets = []
        for _ in range(field.rows):
            self._bullets.append([])

    def spawn_bullet(self, row, col):
        self._bullets[0].append(Bullet(row, col))

    def on_tick(self):
        for row in range(self._field.rows):
            for bullet in self._bullets[row]:
                bullet.on_tick()

    def draw(self, screen):
        for row in range(self._field.rows):
            for bullet in self._bullets[row]:
                bullet.draw(screen)