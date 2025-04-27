import pygame
from PIL import Image
import spriteLoader
import configManager

class Zombie:
    def __init__(self):
        self.hp = 10
        self.position = (0,0)

        config = configManager.ConfigManager.get_instance()
        size = config.get("zombieSize")
        sprite_path = config.get("zombieSprite")
        self.sprite = spriteLoader.load(sprite_path,size)

    def draw(self, screen):
        screen.blit(self.sprite, (0, 0))