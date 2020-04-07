from random import randint
from vehicles2 import classes_of_cars


def generate():
    k = randint(1, 7)

    def random_class():
        if k == 1:
            return classes_of_cars.PedalBikes()
        elif k == 2:
            return classes_of_cars.MotorBikes()
        elif k == 3:
            return classes_of_cars.PickUps()
        elif k == 4:
            return classes_of_cars.SportCars()
        elif k == 5:
            return classes_of_cars.EstateCars()
        elif k == 6:
            return classes_of_cars.MediumTrucks()
        else:
            return classes_of_cars.HeavyTrucks()

    data = ["Class,wheels,speed,power".split(",")]
    lists_of_objects = []

    for j in range(1000):
        temp_object = random_class()
        lists_of_objects.append(temp_object)
        line = temp_object.for_csv()
        data.append(line)

    return data
