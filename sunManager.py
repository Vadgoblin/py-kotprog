import pygame
import random
import field
from config import Config
from sun import Sun
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game

config = Config().sun
rnd = random.Random()

class SunManager:
    def __init__(self, game: "Game"):
        self._game = game
        self._suns = []
        self._collect_speed = config["collect_speed"]
        self._sky_fall_speed = config["sky_fall_speed"]
        self._sky_fall_interval = config["sky_fall_interval"]
        self._sunflower_max_random_distance = config["sunflower_max_random_distance"]

    def spawn_sun(self,row, col):
        d = self._sunflower_max_random_distance
        x = field.col_to_x(col) + rnd.randint(-d,d)
        y = field.row_to_y(row)+ rnd.randint(-d,d)
        new_sun = Sun(x,y)
        self._suns.append(new_sun)

    def draw(self, screen):
        for sun in self._suns:
            sun.draw(screen)

    def on_tick(self):
        for sun in self._suns:
            sun.on_tick()
            if not sun.is_alive:
                self._suns.remove(sun)

    def on_event(self, event: "pygame.event.Event"):
        if event.type != pygame.MOUSEBUTTONDOWN:
            return False

        for sun in self._suns:
            if sun.is_clicked(event):
                self._collect_sun(sun)
                return True

    def _collect_sun(self, sun : "Sun"):
        collected_sun_pos = self._game.plant_selector.sun_position
        sun.animate_and_die(*collected_sun_pos, animation_speed=self._collect_speed)