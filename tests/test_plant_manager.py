import unittest
from unittest.mock import Mock, patch
from src.pvz.game.plant.plantManager import PlantManager
from src.pvz.config.config import Config
from src.pvz.game.plant.plants.peashooter import Peashooter

class TestPlantManager(unittest.TestCase):
    def setUp(self):
        config = Config().field
        self.rows = config["rows"]
        self.cols = config["columns"]
        mock_field = Mock()
        mock_field.rows = self.rows
        mock_field.cols = self.cols
        self.mock_sun_manager = Mock()
        mock_game = Mock()
        mock_game.field = mock_field
        mock_game.sun_manager = self.mock_sun_manager
        self.plant_manager = PlantManager(mock_game)

    def test_init(self):
        self.assertEqual(len(self.plant_manager._plants),self.rows)
        for i in range(0, self.rows):
            self.assertEqual(len(self.plant_manager._plants[i]), self.cols)

    @patch('src.pvz.game.soundPlayer.play_plant')
    def test_plant_plant_valid(self,mock_play_plant):
        self.mock_sun_manager.sun_amount = 1000
        self.plant_manager.plant_plant("peashooter",0,0)

        self.assertIsInstance(self.plant_manager._plants[0][0],Peashooter)
        mock_play_plant.assert_called_once()

    @patch('src.pvz.game.soundPlayer.play_plant')
    def test_plant_plant_invalid_plant(self,mock_play_plant):
        self.mock_sun_manager.sun_amount = 1000

        self.assertRaises(Exception,self.plant_manager.plant_plant,"asd",0,0)
        mock_play_plant.assert_not_called()

    @patch('src.pvz.game.soundPlayer.play_plant')
    def test_plant_plant_invalid_not_enough_sun_amount(self,mock_play_plant):
        self.mock_sun_manager.sun_amount = 1

        self.assertRaises(Exception,self.plant_manager.plant_plant,"sunflower",0,0)
        mock_play_plant.assert_not_called()

    @patch('src.pvz.game.soundPlayer.play_plant')
    def test_plant_plant_invalid_taken_place(self,mock_play_plant):
        self.mock_sun_manager.sun_amount = 10000
        self.plant_manager.plant_plant("peashooter", 0, 0)

        self.assertRaises(Exception,self.plant_manager.plant_plant,"sunflower",0,0)
        mock_play_plant.assert_called_once()