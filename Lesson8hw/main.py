import datetime

def log_simulation(func):
    def wrapper(*args, **kwargs):
        with open("simulation_log.txt", "a") as f:
            f.write(f"Логування почалось о {datetime.datetime.now()}\n")
            try:
                result = func(*args, **kwargs)
                f.write("Логування успішне\n")
                return result
            except Exception as e:
                f.write(f"Виникла помилка: {str(e)}\n")
    return wrapper

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        execution_time = end_time - start_time
        print(f"Час виконання: {execution_time}")
        return result
    return wrapper

@log_simulation
class Car:
    def __init__(self, model):
        self.model = model
        self.owner = None

    def __str__(self):
        if self.owner:
            return f"Автомобіль {self.model} належить {self.owner.name}ові"
        else:
            return f"Автомобіль {self.model} поки що без власника"

@log_simulation
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

if __name__ == "__main__":
    person1 = Person("Кирил")
    person2 = Person("Олександр")
    person3 = Person("Ярослав")
    person4 = Person("Денис")

    car1 = Car("BMW X5M Competition")
    car2 = Car("Audi RSQ8")
    car3 = Car("Mercedes G63 2021")
    car4 = Car("BMW X7 m50d")

    person1.buy_car(car1)
    person2.buy_car(car2)
    person3.buy_car(car3)
    person4.buy_car(car4)

    car3.owner = None
    car4.owner = None

    print(person1)
    print(person2)
    print(person3)
    print(person4)
    print("|")
    print(car1)
    print(car2)
    print(car3)
    print(car4)
