import unittest
from unittest.mock import Mock, patch
from src.pvz.config import Config
from src.pvz.game.zombie.zombie import Zombie
from src.pvz.game.field import row_to_y

class TestZombie(unittest.TestCase):
    def test_init(self):
        config = Config()
        row = 4
        y = row_to_y(row)
        zombie = Zombie(Mock(),row)

        self.assertEqual(zombie.row, row)
        self.assertEqual(zombie.x, config.zombie["spawn_x"])
        self.assertEqual(zombie.y, y)
        self.assertTrue(zombie.width != 0)

    @patch('src.pvz.game.sound_player.play_chomp')
    def test_tick_movement(self, mock_play_chomp):
        mock_zombie_manager = Mock()
        mock_zombie_manager.get_blocking_plant.return_value = None
        zombie = Zombie(mock_zombie_manager,0)

        before_x = zombie.x
        zombie.on_tick()
        after_x = zombie.x

        self.assertTrue(before_x>after_x)
        mock_play_chomp.assert_not_called()

    @patch('src.pvz.game.sound_player.play_chomp')
    def test_tick_blocked(self, mock_play_chomp):
        mock_zombie_manager = Mock()
        mock_plant = Mock()
        mock_zombie_manager.get_blocking_plant.return_value = mock_plant
        zombie = Zombie(mock_zombie_manager, 0)

        before_x = zombie.x
        zombie.on_tick()
        after_x = zombie.x

        self.assertEqual(before_x,after_x)
        mock_plant.suffer_damage.assert_called_once()
        mock_play_chomp.assert_called_once()

    def test_suffer_damage(self):
        zombie = Zombie(Mock(),0)

        before_hp = zombie._hp
        zombie.suffer_damage(1)
        after_hp = zombie._hp

        self.assertEqual(after_hp, before_hp - 1)

    def test_is_alive_alive(self):
        zombie = Zombie(Mock(), 0)

        self.assertTrue(zombie.is_alive)

    def test_is_alive_dead(self):
        zombie = Zombie(Mock(), 0)

        zombie.suffer_damage(zombie._hp)

        self.assertFalse(zombie.is_alive)

if __name__ == '__main__':
    unittest.main()