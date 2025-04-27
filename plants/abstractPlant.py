from abc import ABC, abstractmethod
import configManager
import field

config = configManager.ConfigManager()

class AbstractPlant(ABC):
    def __init__(self,row, col,hp):
        self._row = row
        self._col = col
        self._hp = hp
        self._sprite = None
        self._offset_x = config.get("plant_offset_x")
        self._offset_y = config.get("plant_offset_y")

    @abstractmethod
    def on_tick(self):
        pass

    def draw(self, screen):
        x = field.col_to_x(self._row) + self._offset_x
        y = field.row_to_y(self._row) + self._offset_y
        screen.blit(self._sprite, (x,y))

    def suffer_damage(self):
        self._hp -= 1
        print(self._hp)