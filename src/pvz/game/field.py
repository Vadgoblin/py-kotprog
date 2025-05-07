from math import floor
from typing import TYPE_CHECKING

import pygame

from src.pvz.assets.asset_loader import load_sprite
from src.pvz.config.config import Config
from .plant.ghost_plant_manager import GhostPlantManager

if TYPE_CHECKING:
    from .game import Game

config = Config().field


def _get_sprite():
    sprite_path = Config().game["background"]
    return load_sprite(sprite_path)


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
    field_cols = config["columns"]
    field_block_width = field_width / field_cols
    x = field_x + (col * field_block_width)
    return x


def get_block_width():
    field_width = config["width"]
    field_cols = config["columns"]
    field_block_width = field_width / field_cols
    return field_block_width


def validate_row(row):
    if not isinstance(row, int) or row < 0 or row >= config["rows"]:
        raise ValueError(
            f"Expected row to be an integer between 0 and {config["rows"] - 1}, got {row}"
        )


def validate_column(col):
    if not isinstance(col, int) or col < 0 or col >= config["columns"]:
        raise ValueError(
            f"Expected row to be an integer between 0 and {config["columns"] - 1}, got {col}"
        )


class Field:
    def __init__(self, game: "Game"):
        self._game = game
        self._rows = config["rows"]
        self._cols = config["columns"]
        self._background = _get_sprite()
        self._ghost_plant_manager = GhostPlantManager()

    @property
    def rows(self):
        return self._rows

    @property
    def cols(self):
        return self._cols

    def draw(self, screen):
        screen.blit(self._background, (0, 0))
        self._ghost_plant_manager.draw(screen)

    def on_event(self, event: "pygame.event.Event"):
        mouse_pos = self._get_mouse_pos(event)
        if mouse_pos is None:
            self._ghost_plant_manager.hide()
            return False

        if event.type == pygame.MOUSEBUTTONDOWN:
            self._plant_plant(mouse_pos)
        elif event.type == pygame.MOUSEMOTION:
            self._ghost_plant(mouse_pos)

        return True

    def _get_mouse_pos(self, event: "pygame.event.Event"):
        width = config["width"]
        height = config["height"]
        x = config["x"]
        y = config["y"]

        click_pos = event.dict["pos"]
        click_x, click_y = click_pos

        click_x -= x
        click_y -= y

        if click_x < 0 or click_y < 0 or click_x >= width or click_y >= height:
            return None

        block_width = width / self._cols
        block_height = height / self._rows

        col = floor(click_x / block_width)
        row = floor(click_y / block_height)

        return row, col

    def _plant_plant(self, mouse_pos):
        selected_plant = self._game.plant_selector.selected_plant
        if selected_plant is None:
            return
        if not self._game.plant_manager.is_space_empty(*mouse_pos):
            return
        self._game.plant_manager.plant_plant(selected_plant, *mouse_pos)
        self._ghost_plant_manager.hide()

    def _ghost_plant(self, mouse_pos):
        selected_plant = self._game.plant_selector.selected_plant
        if selected_plant is None:
            self._ghost_plant_manager.hide()
            return
        if not self._game.plant_manager.is_space_empty(*mouse_pos):
            self._ghost_plant_manager.hide()
            return
        self._ghost_plant_manager.show(selected_plant, *mouse_pos)
