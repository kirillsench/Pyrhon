from teacher import Teacher
from student import Student
andrii = Teacher("Andrii", 37, "PythonOOP", "teacher")
yaroslav = Student("Yaroslav", 12.8, "SP2122", "student")
oleksandr = Student("Oleksandr", 14.2, "SP2122", "student")
denys = Student("Denys", 12.6, "SP2122", "student")
dmytro = Student("Dmytro", 12.3, "SP2122", "student")
kyrylo = Student("Kyrylo", 14.1, "SP2122", "student")
humans = list()
for human in andrii, yaroslav, oleksandr, denys, dmytro, kyrylo:
    humans.append(human)
for human in humans:
    print(human)