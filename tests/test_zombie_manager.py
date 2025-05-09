import unittest
from unittest.mock import Mock

from src.pvz.config import Config
from src.pvz.game.zombie.zombie_manager import ZombieManager


class TestZombieManager(unittest.TestCase):
    def setUp(self):
        self.rows = Config().field["rows"]
        self.mock_game = Mock()
        self.mock_game.field.rows = self.rows
        self.zombie_manager = ZombieManager(self.mock_game)

    def test_init(self):
        self.assertEqual(self.zombie_manager._game, self.mock_game)
        self.assertEqual(len(self.zombie_manager._zombies), self.rows)

    def test_spawn_zombie_valid(self):
        self.zombie_manager.spawn_zombie(0)

        self.assertEqual(len(self.zombie_manager._zombies[0]), 1)

    def test_spawn_zombie_invalid(self):
        self.assertRaises(Exception, self.zombie_manager.spawn_zombie,
                          self.rows)

    def test_does_plant_see_zombie_true(self):
        row = 2
        self.zombie_manager.spawn_zombie(row)
        mock_plant = Mock()
        mock_plant.row = row
        mock_plant.col = 0

        self.assertTrue(self.zombie_manager.does_plant_see_zombie(mock_plant))

    def test_does_plant_see_zombie_false(self):
        mock_plant = Mock()
        mock_plant.row = 1
        mock_plant.col = 0

        self.assertFalse(self.zombie_manager.does_plant_see_zombie(mock_plant))

    def test_get_zombie_hit_by_bullet(self):
        self.zombie_manager.spawn_zombie(0)
        self.zombie_manager.spawn_zombie(1)
        self.zombie_manager.spawn_zombie(2)
        zombie = self.zombie_manager._zombies[0][0]
        x = zombie.x
        y = zombie.y

        mock_bullet = Mock()
        mock_bullet.x = x
        mock_bullet.y = y
        mock_bullet.row = 0
        mock_bullet.width = 1
        mock_bullet.height = 1

        self.assertEqual(
            self.zombie_manager.get_zombie_hit_by_bullet(mock_bullet), zombie)

    def test_get_nearby_zombies(self):
        for i in range(0, self.rows):
            self.zombie_manager.spawn_zombie(i)
            self.zombie_manager.spawn_zombie(i)

        self.assertEqual(len(self.zombie_manager.get_nearby_zombies(3, 9)), 6)

    def test_get_number_of_zombies(self):
        self.zombie_manager.spawn_zombie(2)
        self.zombie_manager.spawn_zombie(4)

        self.assertEqual(self.zombie_manager.get_number_of_zombies(), 2)

    def test_on_tick(self):
        mock_zombie1 = Mock()
        mock_zombie1.x = 10000
        mock_zombie2 = Mock()
        mock_zombie2.x = 10000
        self.zombie_manager._zombies[0].append(mock_zombie1)
        self.zombie_manager._zombies[1].append(mock_zombie2)

        self.zombie_manager.on_tick()

        mock_zombie1.on_tick.assert_called_once()
        mock_zombie2.on_tick.assert_called_once()

    def test_on_tick_gameover(self):
        mock_zombie1 = Mock()
        mock_zombie1.x = 0
        self.zombie_manager._zombies[0].append(mock_zombie1)

        self.zombie_manager.on_tick()

        self.mock_game.defeat.assert_called_once()


if __name__ == '__main__':
    unittest.main()
