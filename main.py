import pygame
from field import Field
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
game.zombie_manager.spawn_zombie(0)
game.zombie_manager.spawn_zombie(1)
game.zombie_manager.spawn_zombie(2)
game.zombie_manager.spawn_zombie(3)
game.zombie_manager.spawn_zombie(4)

fc = Config().field
game.sun_manager.spawn_sun(0,0)

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
