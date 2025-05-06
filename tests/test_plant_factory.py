import unittest
from unittest.mock import Mock
from src.pvz.game.plant.plant_factory import plant_factory
from src.pvz.game.plant.plants import peashooter,sunflower,wallnut,cherrybomb

class TestPlantFactory(unittest.TestCase):
    def test_peashooter(self):
        plant = plant_factory(Mock(),"peashooter",0,0)
        self.assertIsInstance(plant,peashooter.Peashooter)

    def test_wallnut(self):
        plant = plant_factory(Mock(),"wallnut",0,0)
        self.assertIsInstance(plant,wallnut.Wallnut)

    def test_sunflower(self):
        plant = plant_factory(Mock(),"sunflower",0,0)
        self.assertIsInstance(plant,sunflower.Sunflower)

    def test_cherrybomb(self):
        plant = plant_factory(Mock(),"cherrybomb",0,0)
        self.assertIsInstance(plant,cherrybomb.Cherrybomb)

    def test_invalid(self):
        self.assertRaises(Exception,plant_factory,Mock(),"asd",0,0)