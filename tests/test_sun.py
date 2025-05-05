import unittest
from src.pvz.config import Config
from src.pvz.game.sun.sun import Sun

class TestSun(unittest.TestCase):
    def test_init(self):
        config = Config().sun

        sun = Sun(x=100, y=200)

        self.assertEqual(sun._x, 100)
        self.assertEqual(sun._y, 200)
        self.assertEqual(sun._width, config["width"])
        self.assertEqual(sun._height, config["height"])
        self.assertEqual(sun._lifespan, config["lifespan"])
        self.assertTrue(sun._pickupable)
        self.assertTrue(sun.is_alive)
