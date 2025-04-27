import pygame
from PIL import Image
import spriteLoader
import configManager

config = configManager.ConfigManager()

class Zombie:
    def __init__(self):
        self.hp = 10
        self.x = 8
        self.y = 3

        size = config.get("zombie_size")
        sprite_path = config.get("zombie_sprite")
        self.sprite = spriteLoader.load(sprite_path,size)

    def draw(self, screen):
        abs_pos = _calculate_absolute_position(self.x, self.y)
        screen.blit(self.sprite, abs_pos)

    def move(self):
        self.x -= 0.01

def _calculate_absolute_position(x,y):
    field_width, field_height = config.get("field_size")
    field_x, field_y = config.get("field_pos")
    field_block_width = field_width / config.get("field_columns")
    field_block_height = field_height / config.get("field_rows")
    abs_x = field_x + (x * field_block_width)
    abs_y = field_y + (y * field_block_height) - 40
    return abs_x,abs_y