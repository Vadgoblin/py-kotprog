import pygame
import spriteLoader
from config import Config
from game import Game

config = Config().game

pygame.init()
pygame.font.init()
X = config["width"]
Y = config["height"]

screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption('PvZ paint edition')

bg = spriteLoader.load("assets/background.png")
clock = pygame.time.Clock()

game = Game()

fc = Config().field

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
            game.on_event(event)


    game.on_tick()

    # print(field.zombie_manager.does_plant_see_zombie(field.plant_manager._plants[0][0]))

    game.draw(screen)

    pygame.display.flip()

    clock.tick(config["target_fps"])
    # print(clock.get_time())
    # print(clock.get_fps())
