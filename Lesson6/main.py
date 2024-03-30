#1 BaseException
'''
try:
    code
except:
    code
finally:
    code
'''



'''
try:
    digit1 = int(input("Enter digit1: "))
    digit2 = int(input("Enter digit2: "))
    print(digit1/digit2)#ZeroDivisionError: division by zero
except Exception as ex:
    print(ex)
finally:
    print("finally")

try:
    digit1 = int(input("Enter digit1: "))
    digit2 = int(input("Enter digit2: "))
    print(digit1/digit2)
except Exception as te:
    print(f'EX: {te}')
except Exception as zde:
    print(f'EX: {zde}')
except Exception as ex:
    print(f'EX: {ex}')
print("End")
'''


from builderror import BuildError
from validator import Validator
limit = 7
try:
    amount = Validator.GetIntValue()
    Validator.Check(amount, limit)
except BuildError as be:
    print(be)
except Exception as ex:
    print(ex)
print("End")