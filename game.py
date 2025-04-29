from bullet.bulletManager import BulletManager
from field import Field
from plant.plantManager import PlantManager
from plantSelector import PlantSelector
from zombie.zombieManager import ZombieManager
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pygame

class Game:
    def __init__(self):
        self._field = Field()
        self._plant_manager = PlantManager(self)
        self._zombie_manager = ZombieManager(self)
        self._bullet_manager = BulletManager(self)
        self._plant_selector = PlantSelector()


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

    def draw(self, screen):
        self._field.draw(screen)
        self._plant_manager.draw(screen)
        self._zombie_manager.draw(screen)
        self._bullet_manager.draw(screen)
        self._plant_selector.draw(screen)

    def on_tick(self):
        self._plant_manager.on_tick()
        self._zombie_manager.on_tick()
        self._bullet_manager.on_tick()

    def on_event(self, event : "pygame.event.Event"):
        if self._plant_selector.on_event(event): return