"""
Main entry point for the PvZ game.
"""

import pygame
import pygame.mixer

from src.pvz.config import Config
from src.pvz.menu import Menu


def main():
    screen = get_screen()
    menu = Menu(screen)
    menu.show()


def get_screen():
    config = Config()
    pygame.init()
    x = config.game["width"]
    y = config.game["height"]

    screen = pygame.display.set_mode((x, y))
    pygame.display.set_caption('PvZ paint edition')
    return screen


if __name__ == "__main__":
    main()
