import pygame
import random
from game import field
from config.config import Config
from game.sun.sun import Sun
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game.game import Game

field_config = Config().field
sun_config = Config().sun
rnd = random.Random()


def _get_next_sky_sun_timeout():
    return rnd.randint(int(sun_config["sky_fall_interval_min"]), int(sun_config["sky_fall_interval_max"]))


class SunManager:
    def __init__(self, game: "Game"):
        self._game = game
        self._collected_amount = 50
        self._suns = []
        self._sky_sun_timeout = _get_next_sky_sun_timeout() / 2
        self._collect_speed = sun_config["collect_speed"]
        self._sky_fall_speed = sun_config["sky_fall_speed"]
        self._sunflower_max_random_distance = sun_config["sunflower_max_random_distance"]

    def spawn_sun(self,row, col):
        d = self._sunflower_max_random_distance
        x = field.col_to_x(col) + rnd.randint(-d, d)
        y = field.row_to_y(row) + rnd.randint(-d, d)
        new_sun = Sun(x,y)
        self._suns.append(new_sun)

    def draw(self, screen):
        for sun in self._suns:
            sun.draw(screen)

    def on_tick(self):
        for sun in self._suns:
            if not sun.is_alive:
                self._suns.remove(sun)
                continue
        self._sky_sun_spawner()
        self._sun_tick()

    def _sky_sun_spawner(self):
        if self._sky_sun_timeout > 0:
            self._sky_sun_timeout -= 1
            return

        self._spawn_sky_sun()
        self._sky_sun_timeout = _get_next_sky_sun_timeout()

    def _spawn_sky_sun(self):
        field_x = field_config["x"]
        field_y = field_config["y"]
        field_width = field_config["width"]
        field_height = field_config["height"]

        target_x = rnd.randint(int(field_x * 1.2), int((field_x + field_width) * 0.9))
        target_y = rnd.randint(int(field_y * 1.2), int((field_y + field_height) * 0.8))
        start_x = target_x
        start_y = field_y / 3

        sun = Sun(start_x,start_y)
        sun.animate(target_x,target_y,self._sky_fall_speed)
        self._suns.append(sun)

    def _sun_tick(self):
        for sun in self._suns:
            sun.on_tick()
            if not sun.is_alive:
                self._suns.remove(sun)

    def _increase_collected_amount(self, amount):
        self._collected_amount += amount

    def decrease_collected_amount(self, amount):
        self._collected_amount -= amount

    @property
    def sun_amount(self):
        return self._collected_amount

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
        self._increase_collected_amount(25)