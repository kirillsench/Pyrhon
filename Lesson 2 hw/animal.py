class Animal(object):
    def __init__(self, name:str, age:float, group:str = ''):
        self.Name:str =  name
        self.Age:float = age
        self.Group:str = group

    def __str__(self):
        return (f"Name: {self.Name}\n"
                f"Age: {self.Age}\n"
                f"Group: {self.Group}")