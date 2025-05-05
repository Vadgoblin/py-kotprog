import unittest
from unittest.mock import Mock, patch
from src.pvz.game.plant.plantSelector import PlantSelector
from src.pvz.config.config import Config

class TestPlantSelector(unittest.TestCase):
    @patch('pygame.font.Font')
    def test_init(self,mock_font):
        mock_game = Mock()
        plant_selector = PlantSelector(mock_game)

        self.assertIsNone(plant_selector.selected_plant)
        self.assertIsNotNone(plant_selector.sun_position)

    @patch('pygame.draw')
    @patch('pygame.font.Font')
    def test_draw(self, mock_font, mock_draw):
        mock_sun_manager = Mock()
        mock_sun_manager.sun_amount = 100
        mock_game = Mock()
        mock_game.sun_manager = mock_sun_manager
        plant_selector = PlantSelector(mock_game)
        mock_screen = Mock()
        plant_selector.draw(mock_screen)

        mock_draw.rect.assert_called()
        mock_draw.line.assert_called()
        mock_font.assert_called()
        mock_screen.blit.assert_called()