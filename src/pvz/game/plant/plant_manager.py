from typing import TYPE_CHECKING, List

from src.pvz.config.config import Config
from src.pvz.game import sound_player, field
from src.pvz.game.plant.plant_factory import plant_factory
from src.pvz.game.plant.plants.abstract_plant import AbstractPlant

if TYPE_CHECKING:
    from src.pvz.game.game import Game

plant_config = Config().plant


def _validate_plant_type(plant_type):
    if plant_type not in plant_config["types"]:
        raise f"{plant_type} is an invalid plant type"


def _get_plant_cost(plant_type):
    _validate_plant_type(plant_type)
    cost = plant_config[plant_type]["cost"]
    return cost


class PlantManager:
    def __init__(self, game: 'Game'):
        self._game = game
        self._plants: "List[List[AbstractPlant | None]]" = []
        for row in range(self._game.field.rows):
            self._plants.append([])
            for _ in range(self._game.field.cols):
                self._plants[row].append(None)

    def plant_plant(self, plant_type, row, col):
        _validate_plant_type(plant_type)
        field.validate_row(row)
        field.validate_column(col)
        self._validate_empty_space(row, col)

        sun_amount = self._game.sun_manager.sun_amount
        plant_cost = _get_plant_cost(plant_type)
        if sun_amount < plant_cost:
            raise Exception(f"Not enough sun. {plant_type} costs {plant_cost} but only have {sun_amount}")

        sound_player.play_plant()
        self._plants[row][col] = plant_factory(self, plant_type, row, col)
        self._game.sun_manager.decrease_collected_amount(plant_cost)
        self._game.plant_selector.disable_plant(plant_type)

    def _validate_empty_space(self, row, col):
        if not self.is_space_empty(row, col):
            raise Exception(f"There is already a plant at row {row} column {col}")

    def does_plant_see_zombie(self, plant):
        return self._game.zombie_manager.does_plant_see_zombie(plant)

    def get_blocking_plant(self, zombie):
        row = zombie.row
        for col in range(self._game.field.cols - 1, -1, -1):
            plant = self._plants[row][col]
            if plant is None:
                continue
            plant_x = field.col_to_x(plant.col)
            if zombie.x <= plant_x + plant.width * (4 / 5) and zombie.x + zombie.width >= plant_x + plant.width / 3:
                return plant
        return None

    def is_space_empty(self, row, col):
        return self._plants[row][col] is None

    def spawn_bullet(self, row, col):
        self._game.bullet_manager.spawn_bullet(row, col)

    def spawn_sun(self, row, col):
        self._game.sun_manager.spawn_sun(row, col)

    def draw(self, screen):
        for row in range(self._game.field.rows):
            for col in range(self._game.field.cols):
                plant = self._plants[row][col]
                if plant is not None:
                    plant.draw(screen)

    def on_tick(self):
        for row in range(self._game.field.rows):
            for col in range(self._game.field.cols):
                plant = self._plants[row][col]
                if plant is not None:
                    if plant.is_alive:
                        plant.on_tick()
                    else:
                        self._plants[plant.row][plant.col] = None
