from student import Student
yaroslav = Student("Yaroslav", 12.8, "SP2122")
oleksandr = Student("Oleksandr", 14.2, "SP2122")
denys= Student("Denys", 12.6, "SP2122")
dmytro = Student("Dmytro", 12.3, "SP2122")
kyrylo = Student("kyrylo", 14.1, "SP2122")

#students = [yaroslav, oleksandr, denys, dmytro, kyrylo]
students = list()
students.append(yaroslav)
students.append(oleksandr)
students.append(denys)
students.append(dmytro)
students.append(kyrylo)
for student in students:
    print(f"Name: {student.Name}\n"
          f"Age: {student.Age}\n"
          f"Group: {student.Group}\n")
print("Hello world\nEnd:)")
