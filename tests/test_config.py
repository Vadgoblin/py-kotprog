import unittest
from src.pvz.config import Config

class TestConfig(unittest.TestCase):
    def test_constructor(self):
        instance = Config()
        self.assertIsNotNone(instance)

    def test_get_instance(self):
        instance = Config.get_instance()
        self.assertIsNotNone(instance)

    def test_singleton(self):
        instance1 = Config()
        instance2 = Config()
        self.assertEqual(instance1,instance2)