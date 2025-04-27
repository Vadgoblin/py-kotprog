import plants.peashooter


def plantFactory(plant_type, row, col):
    if plant_type == "peashooter":
        return plants.peashooter.Peashooter(row, col)

    else:
        raise Exception(f"\"{plant_type}\" is an invalid plant type")