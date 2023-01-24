class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.iteration = 0

    def __iter__(self):
        return self

    def __next__(self):
        while 0 <= self.count:
            result = self.count
            self.count -= 1
            return result

        raise StopIteration


iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")




