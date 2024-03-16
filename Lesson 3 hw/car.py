class Car:
    def __init__(self, model):
        self.model = model
        self.owner = None

    def __str__(self):
        if self.owner:
            return f"Автомобіль {self.model} належить {self.owner.name}ові"
        else:
            return f"Автомобіль {self.model} поки що без власника"