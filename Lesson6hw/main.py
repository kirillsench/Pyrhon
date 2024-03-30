result = []

def divider(a, b):
    try:
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("TypeError: a та b мають бути цілими")
        if a < b:
            raise ValueError("ValueError: a менше b")
        if b > 100:
            raise IndexError("IndexError: b більше ніж 100")
        if b == 0:
            raise ZeroDivisionError("ZeroDivisionError: division by zero")
        return a / b
    except TypeError as te:
        print(te)
    except ValueError as ve:
        print(ve)
    except IndexError as ie:
        print(ie)
    except ZeroDivisionError as zd:
        print(zd)

data = {(10,): 2, (2,): 5, ("123",): 4, (18,): 0, (8,): 4}
for key in data:
    try:
        res = divider(key[0], data[key])
        if res is not None:
            result.append(res)
    except Exception as e:
        print("Exception:", e)

print(result)