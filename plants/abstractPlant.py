from abc import ABC, abstractmethod

class AbstractPlant(ABC):
    def __init__(self,row, col,hp):
        self._row = row
        self._col = col
        self._hp = hp

    @abstractmethod
    def on_tick(self):
        pass

    def suffer_damage(self):
        self._hp -= 1
        print(self._hp)