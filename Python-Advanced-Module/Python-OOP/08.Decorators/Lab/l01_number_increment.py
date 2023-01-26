def number_increment(numbers):

    def increase():
        increased_nums_list = [x+1 for x in numbers]
        return increased_nums_list

    return increase()


print(number_increment([1, 2, 3]))