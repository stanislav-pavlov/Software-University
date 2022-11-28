def even_odd(*args):
    command = args[-1]
    numbers = [int(i) for i in args[:-1]]

    if command == "even":
        result = [x for x in numbers if x % 2 == 0]
    elif command == "odd":
        result = [x for x in numbers if x % 2 != 0]
    return result


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))