import pygame
import game.level.levelLoader
from game import Game
from ._button import Button
from config import Config


def _exit():
    pygame.quit()
    exit(0)


class Menu:
    def __init__(self,screen : "pygame.Surface"):
        self._screen = screen
        self._config = Config()
        self._background = self._get_background()
        self._buttons = self._get_buttons()
        self._game = Game(screen)

    def _get_background(self):
        bg_path = self._config.menu["background"]
        return pygame.image.load(bg_path).convert()

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

    def _process_event(self,event):
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

    def _play(self, difficulty):
        level = game.level.levelLoader.load_level(f"levels/{difficulty}.json")
        self._game.start(level)