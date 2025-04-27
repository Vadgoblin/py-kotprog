import plants.peashooter


def plantFactory(plant_type, row, col):
    print(plant_type)
    if plant_type == "peashooter":
        return plants.peashooter.Peashooter(row, col)

    else:
        print("HELLO")
        raise Exception(f"\"{plant_type}\" is an invalid plant type")