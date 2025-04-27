import pygame

import spriteLoader
from zombie import Zombie
import configManager

config = configManager.ConfigManager()

pygame.init()
X = config.get("window_width")
Y = config.get("window_height")

screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption('PvZ paint edition')


bg = spriteLoader.load("assets/background.png")
i = 0
clock = pygame.time.Clock()
zombie = Zombie()


while True:
    screen.blit(bg,(0,0))
    zombie.move()
    zombie.draw(screen)

    pygame.display.flip()

    clock.tick(config.get("target_tick_time"))
    # print(clock.get_time())
    # print(clock.get_fps())
    i = i + 1
