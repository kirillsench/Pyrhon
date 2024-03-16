import random

class Math:
    def __init__(self, number):
        self.number = number

    def perform_random_operation(self):
        operation = random.choice(['+', '-', '*', '/'])

        if operation == '+':
            self.number += random.randint(1, 10)
        elif operation == '-':
            self.number -= random.randint(1, 10)
        elif operation == '*':
            self.number *= random.randint(1, 10)
        elif operation == '/':
            divisor = random.randint(1, 10)
            if divisor != 0:
                self.number /= divisor

    def __str__(self):
        return str(self.number)

number = Math(5)
number.perform_random_operation()
print(number)