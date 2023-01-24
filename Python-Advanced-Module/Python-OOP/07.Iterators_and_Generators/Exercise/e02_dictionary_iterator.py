class dictionary_iter:
    def __init__(self, data):
        self.items = list(data.items())
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.idx < len(self.items):
            res = self.items[self.idx]
            self.idx += 1
            return res

        raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
