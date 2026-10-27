class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        return f"Транспортний засіб рухається зі швидкістю {self.speed} км/год."


class Car(Vehicle):
    def __init__(self, speed, brand):
        super().__init__(speed)
        self.brand = brand

    def move(self):
        return f"Автомобіль {self.brand} їде по дорозі зі швидкістю {self.speed} км/год."


class Bicycle(Vehicle):
    def __init__(self, speed, bike_type):
        super().__init__(speed)
        self.bike_type = bike_type

    def move(self):
        return f"Велосипед ({self.bike_type}) їде по доріжці зі швидкістю {self.speed} км/год."


if __name__ == "__main__":
    car = Car(120, "Тесла")
    bicycle = Bicycle(20, "Гірський")

    print(car.move())
    print(bicycle.move())