from math import floor
import pygame
import spriteLoader
from config import Config
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game

config = Config().field

def _get_sprite():
    sprite_path = Config().game["background"]
    return spriteLoader.load(sprite_path)


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
    def __init__(self, game :"Game"):
        self._game = game
        self._rows = config["rows"]
        self._cols = config["columns"]
        self._background = _get_sprite()


    @property
    def rows(self):
        return self._rows

    @property
    def cols(self):
        return self._cols


    def draw(self, screen):
        screen.blit(self._background, (0, 0))


    def on_event(self, event : "pygame.event.Event"):
        mouse_pos = self._get_mouse_pos(event)
        if mouse_pos is None:
            return False

        if event.type == pygame.MOUSEBUTTONDOWN:
            self._plant_plant(mouse_pos)



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

        return (row,col)

    def _plant_plant(self, mouse_pos):
        selected_plant = self._game.plant_selector.selected_plant
        if selected_plant is not None:
            if self._game.plant_manager.is_space_empty(*mouse_pos):
                self._game.plant_manager.plant_plant(selected_plant, *mouse_pos)

    def _ghost_plant(self, mouse_pos):
        pass