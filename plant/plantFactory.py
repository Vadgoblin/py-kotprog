from plant.plants.cherrybomb import Cherrybomb
from plant.plants.peashooter import Peashooter
from plant.plants.sunflower import Sunflower
from plant.plants.wallnut import Wallnut


def plant_factory(plant_manager, plant_type, row, col):
    if plant_type == "peashooter":
        return Peashooter(plant_manager, row, col)
    if plant_type == "sunflower":
        return Sunflower(plant_manager, row, col)
    if plant_type == "wallnut":
        return Wallnut(plant_manager, row, col)
    if plant_type == "cherrybomb":
        return Cherrybomb(plant_manager,row,col)

    else:
        raise Exception(f"\"{plant_type}\" is an invalid plant type")