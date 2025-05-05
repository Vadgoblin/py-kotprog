import unittest
from unittest.mock import Mock
from src.pvz.game.bullet.bullet import Bullet

class TestBullet(unittest.TestCase):
    def test_idk(self):
        row = 1
        col = 1
        bullet = Bullet(Mock(),row, col)

        self.assertEqual(bullet.row, row)
        self.assertNotEqual(bullet.x,0)
        self.assertNotEqual(bullet.width,0)
        self.assertTrue(bullet.is_alive)