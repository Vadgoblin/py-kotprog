import pygame
from field import Field
import spriteLoader
from config import Config

config = Config().game

pygame.init()
pygame.font.init()
X = config["width"]
Y = config["height"]

screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption('PvZ paint edition')

bg = spriteLoader.load("assets/background.png")
clock = pygame.time.Clock()

f = Field()
f.zombie_manager.spawn_zombie(0)
f.zombie_manager.spawn_zombie(1)
f.zombie_manager.spawn_zombie(2)
f.zombie_manager.spawn_zombie(3)
f.zombie_manager.spawn_zombie(4)

for i in range(9):
    for j in range(5):
        f.plant_manager.plant_plant("peashooter",j,i)
# f.plant_manager.plant_plant("peashooter", 4, 5)
fc = Config().field


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
            f.on_event(event)


    f.on_tick()

    # print(field.zombie_manager.does_plant_see_zombie(field.plant_manager._plants[0][0]))
    screen.blit(bg, (0, 0))
    f.draw(screen)

    pygame.display.flip()

    clock.tick(config["target_fps"])
    # print(clock.get_time())
    # print(clock.get_fps())
