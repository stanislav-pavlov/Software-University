class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.iterations = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.iterations < self.count:
            result = self.iterations * self.step
            self.iterations += 1
            return result

        raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
