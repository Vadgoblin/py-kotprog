import pygame
from zombie import Zombie
import configManager

config = configManager.ConfigManager()

pygame.init()
X = config.get("windowWidth")
Y = config.get("windowHeight")

screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption('image')

pygame.init()
i = 0
clock = pygame.time.Clock()
zombie = Zombie()

while True:
    screen.fill((128,128,128))
    zombie.draw(screen)
    pygame.display.flip()
    # setting fps of program to max 1 per second
    clock.tick(1)

    # printing time used in the previous tick
    print(clock.get_time())

    # printing compute the clock framerate
    print(clock.get_fps())
    i = i + 1
