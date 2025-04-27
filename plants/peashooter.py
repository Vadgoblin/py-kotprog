from abstractPlant import AbstractPlant

class Peashooter(AbstractPlant):
    def __init__(self,row, col,hp):
        super(AbstractPlant, self).__init__(row,col,hp)
        self.shoot_timeout = 0

    def on_tick(self):
        if self.shoot_timeout == 0:
            pass