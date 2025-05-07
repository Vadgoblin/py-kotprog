import sys
import pygame

from src.pvz.assets.asset_loader import load_sprite
from src.pvz.config import Config
from src.pvz.game import Game
from src.pvz.game.level.level_loader import load_level
from ._button import Button


def _exit():
    pygame.quit() # [no-member]
    sys.exit()


class Menu:
    def __init__(self, screen: "pygame.Surface"):
        self._screen = screen
        self._config = Config()
        self._background = self._get_background()
        self._buttons = self._get_buttons()
        self._game = Game(screen)

    def _get_background(self):
        sprite_name = self._config.menu["background"]
        return load_sprite(sprite_name)

    def _get_buttons(self):
        buttons = {}
        for button_name in ["exit", "easy", "normal", "hard"]:
            button = self._make_button(button_name)
            buttons[button_name] = button
        return buttons

    def _make_button(self, name):
        edges = self._config.menu[f"{name}_button_edges"]
        button = Button(edges)
        return button

    def show(self):
        while True:
            self._process_events()
            self._draw_background()
            pygame.display.flip()

    def _draw_background(self):
        self._screen.blit(self._background, (0, 0))

    def _process_events(self):
        for event in pygame.event.get():
            self._process_event(event)

    def _process_event(self, event):
        if event.type == pygame.QUIT:
            _exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = event.dict['pos']
            self._process_click(click_pos)

    def _process_click(self, click_pos):
        clicked_button = self._get_clicked_button_name(click_pos)
        if clicked_button == "exit":
            _exit()
        elif clicked_button == "easy":
            self._play("easy")
        elif clicked_button == "normal":
            self._play("normal")
        elif clicked_button == "hard":
            self._play("hard")

    def _get_clicked_button_name(self, click_pos):
        for name, btn in self._buttons.items():
            if btn.is_clicked(click_pos):
                return name
        return None

    def _play(self, difficulty):
        level = load_level(f"{difficulty}")
        self._game.start(level)
