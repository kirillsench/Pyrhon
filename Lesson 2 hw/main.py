from animal import Animal
cat = Animal("Cat", 4, "ZOO 1")
dog = Animal("Dog", 6, "ZOO 2")

animals = list()
animals.append(cat)
animals.append(dog)

for animal in animals:
    print(f"Name: {animal.Name}\n"
          f"Age: {animal.Age}\n"
          f"Group: {animal.Group}\n")
print("Hello world\nEnd:)")