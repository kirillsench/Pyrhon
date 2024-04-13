from repository import Repository
database = 'students.sl3'
timeout = 5.0
repo = Repository(database, timeout)
#1 CREATE TABLE ...(fields definitions)
'''
repo.Query('CREATE TABLE SP2122(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(20), age INT, avg_grade FLOAT)')
'''
#2 INSERT INTO ...(fields) VALUES(values)

#repo.Query("INSERT INTO SP2122(name, age, avg_grade) VALUES('Kavurko Oleksandr', 14, 11)")
#repo.Query("INSERT INTO SP2122(name, age, avg_grade) VALUES('Ubizkiy Vladyslav', 12, 11)")

#3 UPDATE ... SET ... WHERE ...
'''
#3.1 without filter
repo.Query("UPDATE SP2122 SET avg_grade=10")#all records will be changed
'''

#3.2 with filter
repo.Query("UPDATE SP2122 SET avg_grade=10 WHERE name LIKE 'Ubizkiy%'")
