import math
from config import Config
import spriteLoader
import pygame

config = Config().sun

class Sun:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._width = config["width"]
        self._height = config["height"]
        self._lifespan = config["lifespan"]
        self._sprite = self._load_sprite()
        self._pickupable = True
        self._alive = True
        self._animated = False
        self._animation_speed = None
        self._animate_to_x = None
        self._animate_to_y = None
        self._die_after_animation = False

    def _load_sprite(self):
        path = config["sprite"]
        size = self._width, self._height
        return spriteLoader.load(path, size)

    @property
    def is_alive(self):
        return self._alive

    def is_pickupable(self):
        return self._pickupable

    def is_clicked(self, event: "pygame.event.Event"):
        if not self._pickupable:
            return False
        if event.type != pygame.MOUSEBUTTONDOWN:
            return False
        click_pos = event.dict["pos"]
        click_x, click_y = click_pos

        if self._x > click_x:
            return False
        if self._y > click_y:
            return False
        if self._x + self._width < click_x:
            return False
        if self._y + self._height < click_y:
            return False
        return True

    def animate(self, to_x, to_y, animation_speed):
        self._animate_to_x = to_x
        self._animate_to_y = to_y
        self._animation_speed = animation_speed
        self._animated = True

    def animate_and_die(self, to_x, to_y, animation_speed):
        self.animate(to_x, to_y, animation_speed)
        self._die_after_animation = True

    def on_tick(self):
        if self._lifespan <= 0:
            self._alive = False
            return
        self._lifespan -= 1

        if not self._animated:
            return
        self._move_towards_animation_target()

        if not self._is_animation_finished():
            return
        self._animated = False

        if self._die_after_animation:
            self._alive = False

    def _move_towards_animation_target(self):
        max_distance = self._animation_speed

        dx = self._animate_to_x - self._x
        dy = self._animate_to_y - self._y
        distance = math.hypot(dx, dy)

        if distance <= max_distance or distance == 0:
            self._x = self._animate_to_x
            self._y = self._animate_to_y
        else:
            scale = max_distance / distance
            self._x = self._x + dx * scale
            self._y = self._y + dy * scale

    def _is_animation_finished(self):
        return self._x == self._animate_to_x and self._y == self._animate_to_y

    def draw(self, screen):
        screen.blit(self._sprite, (self._x, self._y))