def multiply(*args):
    result = 1
    for arg in args:
        result *= int(arg)

    return result


print(multiply(1, 4, 5))