from .bullet.bulletManager import BulletManager
from .enemySpawner import EnemySpawner
from .field import Field
from .plant.plantManager import PlantManager
from .plant.plantSelector import PlantSelector
from .sun.sunManager import SunManager
from .zombie.zombieManager import ZombieManager
from typing import TYPE_CHECKING
from .gameStatus import GameStatus


if TYPE_CHECKING:
    import pygame
    from game.level.level import Level

class Game:
    def __init__(self, level :"Level"):
        self._field = Field(self)
        self._plant_manager = PlantManager(self)
        self._zombie_manager = ZombieManager(self)
        self._bullet_manager = BulletManager(self)
        self._plant_selector = PlantSelector(self)
        self._sun_manager = SunManager(self)
        self._enemy_spawner = EnemySpawner(self, level)

        self._game_status = GameStatus.ONGOING

    @property
    def field(self):
        return self._field

    @property
    def plant_manager(self):
        return self._plant_manager

    @property
    def zombie_manager(self):
        return self._zombie_manager

    @property
    def bullet_manager(self):
        return self._bullet_manager

    @property
    def plant_selector(self):
        return self._plant_selector

    @property
    def sun_manager(self):
        return self._sun_manager

    def draw(self, screen):
        self._field.draw(screen)
        self._plant_manager.draw(screen)
        self._zombie_manager.draw(screen)
        self._bullet_manager.draw(screen)
        self._plant_selector.draw(screen)
        self._sun_manager.draw(screen)

    def on_tick(self):
        if self._game_status != GameStatus.ONGOING:
            return
        self._plant_manager.on_tick()
        self._zombie_manager.on_tick()
        self._bullet_manager.on_tick()
        self._sun_manager.on_tick()
        self._plant_selector.on_tick()
        self._enemy_spawner.on_tick()

    def on_event(self, event : "pygame.event.Event"):
        if self._sun_manager.on_event(event): return
        if self._plant_selector.on_event(event): return
        self._field.on_event(event)

    def victory(self):
        self._game_status = GameStatus.VICTORY
        print("victory")

    def defeat(self):
        self._game_status = GameStatus.DEFEAT
        print("defeat")