from math import floor

from config import Config
from bullet.bulletManager import BulletManager
from plant.plantManager import PlantManager
from plantSelector import PlantSelector
from zombie.zombieManager import ZombieManager
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pygame

config = Config().field


def row_to_y(row):
    field_y = config["y"]
    field_height = config["height"]
    field_rows = config["rows"]
    field_block_height = field_height / field_rows
    y = field_y + (row * field_block_height)
    return y

def col_to_x(col):
    field_x = config["x"]
    field_width = config["width"]
    field_cols =  config["columns"]
    field_block_width = field_width /field_cols
    x = field_x + (col * field_block_width)
    return x


class Field:
    def __init__(self):
        self._rows = config["rows"]
        self._cols = config["columns"]
        self._plant_manager = PlantManager(self)
        self._zombie_manager = ZombieManager(self)
        self._bullet_manager = BulletManager(self)
        self._plant_selector = PlantSelector()

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

    @property
    def bullet_manager(self):
        return self._bullet_manager

    def draw(self, screen):
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
        print(self._get_mouse_pos(event))

    def _get_mouse_pos(self, event: "pygame.event.Event"):
        width = config["width"]
        height = config["height"]
        x = config["x"]
        y = config["y"]

        click_pos = event.dict["pos"]
        click_x, click_y = click_pos

        click_x -= x
        click_y -= y

        if click_x < 0 or click_y < 0 or click_x > width or click_y > height:
            return None

        block_width = width / self._cols
        block_height = height / self._rows



        col = floor(click_x / block_width)
        row = floor(click_y / block_height)

        return (col,row)