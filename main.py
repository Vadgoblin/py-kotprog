import pygame

from field import Field
import spriteLoader
from configManager import ConfigManager

config = ConfigManager().game

pygame.init()
X = config["width"]
Y = config["height"]

screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption('PvZ paint edition')

bg = spriteLoader.load("assets/background.png")
clock = pygame.time.Clock()

field = Field()
field._zombie_manager.spawn_zombie(4)
field._plant_manager.plant_plant("peashooter",0,0)

while True:
    field.on_tick()

    screen.blit(bg, (0, 0))
    field.draw(screen)
    pygame.display.flip()

    clock.tick(config["target_fps"])
    # print(clock.get_time())
    # print(clock.get_fps())
