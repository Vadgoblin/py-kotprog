import field
import spriteLoader
import configManager

config = configManager.ConfigManager().zombie
offset_x = config["offset_x"]
offset_y = config["offset_y"]
spawn_x = config["spawn_x"]

def _load_sprite():
    size = (config["width"], config["height"])
    sprite_path = config["sprite"]
    return spriteLoader.load(sprite_path,size)


class Zombie:
    def __init__(self, row):
        self.row = row
        self.y = field.row_to_y(row)
        self.x = spawn_x
        self.sprite = _load_sprite()

    def draw(self, screen):
        position = (self.x + offset_x, self.y + offset_y)
        screen.blit(self.sprite, position)

    def on_tick(self):
        self.move()

    def move(self):
        self.x -= 1