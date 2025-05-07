from typing import TYPE_CHECKING

from . import sound_player
from .bullet.bullet_manager import BulletManager
from .enemy_spawner import EnemySpawner
from .field import Field
from .game_status import GameStatus
from .plant.plant_manager import PlantManager
from .plant.plant_selector import PlantSelector
from .sound_player import _SoundPlayer
from .sun.sun_manager import SunManager
from .zombie.zombie_manager import ZombieManager

if TYPE_CHECKING:
    import pygame
    from src.pvz.game.level.level import Level


class Game:
    def __init__(self, level: "Level"):
        self._field = Field(self)
        self._plant_manager = PlantManager(self)
        self._zombie_manager = ZombieManager(self)
        self._bullet_manager = BulletManager(self)
        self._plant_selector = PlantSelector(self)
        self._sun_manager = SunManager(self)
        self._enemy_spawner = EnemySpawner(self, level)
        self._sound_player = _SoundPlayer()

        self._game_status = GameStatus.ONGOING

        sound_player.play_bgm()

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

    @property
    def sound_player(self):
        return self._sound_player

    @property
    def game_status(self):
        return self._game_status

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

    def on_event(self, event: "pygame.event.Event"):
        if self._sun_manager.on_event(event):
            return
        if self._plant_selector.on_event(event):
            return
        self._field.on_event(event)

    def victory(self):
        self._game_status = GameStatus.VICTORY
        sound_player.stop_music()
        sound_player.play_win_music()

    def defeat(self):
        self._game_status = GameStatus.DEFEAT
        sound_player.stop_music()
