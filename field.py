from math import floor

import spriteLoader
from config import Config
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pygame

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
    def __init__(self):
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

    def on_tick(self):
        pass

    def on_event(self, event : "pygame.event.Event"):
        pass
        # print(self._get_mouse_pos(event))

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