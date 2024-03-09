class Student:
    def __init__(self, name: str, age: float, group: str = ''):
        self.Name = name
        self.Age = age
        self.Group = group
        self.Money = 0

    def work(self, hours: int, wage_per_hour: float):
        earnings = hours * wage_per_hour
        self.Money += earnings
        print(f"{self.Name} заробив {earnings} грн")

    def spend_money(self, amount: float):
        if self.Money >= amount:
            self.Money -= amount
            print(f"{self.Name} витратив {amount} грн")
        else:
            print(f"{self.Name} не має достатньо коштів для витрати {amount} грн")

    def study(self, hours: int):
        if hours < 3:
            print(f"{self.Name} не вдалося зосередитися. Йому важко навчатися.")
        elif hours < 6:
            print(f"{self.Name} вчився трошки, але йому потрібно більше часу.")
        else:
            print(f"{self.Name} добре навчився сьогодні. Йому подобається вчитися.")

        self.spend_money(10)

    def __str__(self):
        return (f"Name: {self.Name}\n"
                f"Age: {self.Age}\n"
                f"Group: {self.Group}\n"
                f"Money: {self.Money} грн")


if __name__ == "__main__":
    students_data = [
        {"name": "Yaroslav", "age": 12.8, "group": "SP2122"},
        {"name": "Oleksandr", "age": 14.2, "group": "SP2122"},
        {"name": "Denys", "age": 12.6, "group": "SP2122"},
        {"name": "Dmytro", "age": 12.3, "group": "SP2122"},
        {"name": "Kyrylo", "age": 14.1, "group": "SP2122"}
    ]

    students = [Student(**data) for data in students_data]

    for student in students:
        print(student)
        print()

    students[0].work(8, 30)  # Перший студент працює 8 годин за 30 грн на годину
    students[1].work(6, 25)  # Другий студент працює 6 годин за 25 грн на годину

    students[0].study(5)
    students[1].study(7)

    print("\nІнформація про студентів після заробітку та навчання:")
    for student in students:
        print(student)
        print()