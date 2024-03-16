from person import Person
from car import Car

person1 = Person("Кирил")
person2 = Person("Олександр")
person3 = Person("Ярослав")
person4 = Person("Денис")

car1 = Car("BMW X5M Competition")
car2 = Car("Audi RSQ8")
car3 = Car("Mercedes G63 2021")
car4 = Car("BMW X7 m50d")

# Придбання автомобілів
person1.buy_car(car1)
person2.buy_car(car2)
person3.buy_car(car3)
person4.buy_car(car4)

# Зміна власників автомобілів Gelik і X7
car3.owner = None
car4.owner = None

# Перевірка власності автомобілів
print(person1)
print(person2)
print(person3)
print(person4)
print("|")
print(car1)
print(car2)
print(car3)
print(car4)