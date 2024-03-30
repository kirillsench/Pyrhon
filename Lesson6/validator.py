from builderror import BuildError
class Validator:
    @staticmethod
    def Check(amount: int, limit: int):
        if(not amount > 0):
            raise ValueError(f"Amount must be grater than 0. Amount = {amount}")
        if(amount > limit):
            raise BuildError(amount, limit)
        return True
    @staticmethod
    def GetIntValue():
        amountStr = input("Enter amount: ")
        while (True):
            if (amountStr.isdigit()):
                return int(amountStr)
            amountStr = input("Enter integer value for amount: ")

