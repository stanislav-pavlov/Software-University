def criterion(x):
    if x % 2 == 0:
        return True
    else:
        return False


initial_list = map(int, list(input().split(" ")))

even_nums_list = filter(criterion, initial_list)
print(list(even_nums_list))

