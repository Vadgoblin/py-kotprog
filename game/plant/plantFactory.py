from game.plant.plants.cherrybomb import Cherrybomb
from game.plant.plants.peashooter import Peashooter
from game.plant.plants.sunflower import Sunflower
from game.plant.plants.wallnut import Wallnut


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