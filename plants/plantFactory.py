import plants.peashooter


def plantFactory(plant_manager, plant_type, row, col):
    if plant_type == "peashooter":
        return plants.peashooter.Peashooter(plant_manager,row, col)

    else:
        raise Exception(f"\"{plant_type}\" is an invalid plant type")