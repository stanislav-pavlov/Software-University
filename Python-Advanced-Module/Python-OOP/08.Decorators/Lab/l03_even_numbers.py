from functools import wraps


def is_even(num):
    return num % 2 == 0


def even_numbers(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        even_nums_list = [num for num in result if is_even(num)]
        return even_nums_list

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
