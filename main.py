import pygame
from config import Config
from game import Game

config = Config()

pygame.init()
X = config.game["width"]
Y = config.game["height"]

screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption('PvZ paint edition')

game = Game(screen, config)
game.start()
