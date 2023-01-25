class sequence_repeat:
    def __init__(self, sequence, count):
        self.sequence = sequence
        self.count = count
        self.idx = 0
        # self.count_through_seq = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.idx < self.count:
            # My solution:
            # result = self.sequence[self.count_through_seq]
            # self.count_through_seq += 1
            # if self.count_through_seq == len(self.sequence):
            #     self.count_through_seq =0

            # SoftUni solution:
            result = self.sequence[self.idx % len(self.sequence)]
            self.idx += 1
            return result

        raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
