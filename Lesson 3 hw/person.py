class Person:
    def __init__(self, name):
        self.name = name
        self.car = None

    def buy_car(self, car):
        self.car = car
        car.owner = self

    def __str__(self):
        if self.car:
            return f"{self.name} має автомобіль {self.car.model} "
        else:
            return f"{self.name} поки що не має автомобіля"