from plant.peashooter import Peashooter
from plant.sunflower import Sunflower


def plant_factory(plant_manager, plant_type, row, col):
    if plant_type == "peashooter":
        return Peashooter(plant_manager, row, col)
    if plant_type == "sunflower":
        return Sunflower(plant_manager, row, col)

    else:
        raise Exception(f"\"{plant_type}\" is an invalid plant type")