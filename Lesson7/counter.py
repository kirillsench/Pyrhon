class Counter:
    def __init__(self, sequence: list):
        if(len(sequence) == 1):
            self.Min: int = 0
            self.Max: int = sequence[0]
        if (len(sequence) > 1):
            self.Min: int =  sequence[0]
            self.Max: int = sequence[1]
    def __str__(self):
        return f'{self.Min}'

    def __iter__(self):
        self.Min = 0
        return self

    def __next__(self):
        self.Min += 1
        if(self.Min > self.Max):
            raise StopIteration()
        return self