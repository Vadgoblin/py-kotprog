import sys
from typing import TYPE_CHECKING

import pygame

from src.pvz.assets.asset_loader import load_font
from src.pvz.config import Config

if TYPE_CHECKING:
    from pygame.surface import Surface


def display_victory_screen(screen: "Surface"):
    display_result_screen(screen, "Victory")


def display_defeat_screen(screen: "Surface"):
    display_result_screen(screen, "Defeat")


def display_result_screen(screen: "Surface", message: str):
    _draw_text(screen, message)
    pygame.display.flip()
    while not _have_button_pressed():
        pass


def _have_button_pressed():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            return True
    return False


def _draw_text(screen: "Surface", text):
    font_filename = Config().game["text_font"]
    font = load_font(font_filename, 64)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()

    text_rect.center = (screen.get_width() // 2, screen.get_height() // 2)

    padding = 20
    box_rect = text_rect.inflate(padding * 2, padding * 2)

    box_surface = pygame.Surface(box_rect.size, pygame.SRCALPHA)
    box_surface.fill((0, 0, 0, 180))
    screen.blit(box_surface, box_rect.topleft)

    screen.blit(text_surface, text_rect)
