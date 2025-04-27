import pygame

from field import Field
import spriteLoader
from configManager import ConfigManager

config = ConfigManager()

pygame.init()
X = config.get("window_width")
Y = config.get("window_height")

screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption('PvZ paint edition')

bg = spriteLoader.load("assets/background.png")
clock = pygame.time.Clock()

field = Field()
field.spawn_zombie(4)

while True:
    field.on_tick()

    screen.blit(bg, (0, 0))
    field.draw(screen)
    pygame.display.flip()

    clock.tick(config.get("target_tick_time"))
    # print(clock.get_time())
    # print(clock.get_fps())
