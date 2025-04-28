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
        self._y = field.row_to_y(row)
        self._x = spawn_x
        self._sprite = _load_sprite()

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def draw(self, screen):
        position = (self._x + offset_x, self._y + offset_y)
        screen.blit(self._sprite, position)

    def on_tick(self):
        self.move()

    def move(self):
        self._x -= 1