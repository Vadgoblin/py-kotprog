import unittest
from src.pvz.config.config import Config
from unittest.mock import Mock
from src.pvz.game.bullet.bullet_manager import BulletManager


class TestBulletManager(unittest.TestCase):
    def setUp(self):
        config = Config().field
        self.rows = config["rows"]
        mock_field = Mock()
        mock_field.rows = self.rows
        mock_game = Mock()
        mock_game.field = mock_field
        self.bullet_manager = BulletManager(mock_game)

    def test_init(self):
        self.assertEqual(len(self.bullet_manager._bullets), self.rows)

    def test_spawn_bullet(self):
        self.bullet_manager.spawn_bullet(0,0)

        self.assertEqual(len(self.bullet_manager._bullets[0]),1)