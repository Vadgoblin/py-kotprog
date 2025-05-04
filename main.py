import pygame
from config import Config
from menu import Menu

_screen : "pygame.Surface|None"= None

def main():
    _initialize_screen()
    menu = Menu(_screen)
    menu.show()

def _initialize_screen():
    global _screen
    config = Config()
    pygame.init()
    x = config.game["width"]
    y = config.game["height"]

    _screen = pygame.display.set_mode((x, y))
    pygame.display.set_caption('PvZ paint edition')

if __name__ == "__main__":
    main()