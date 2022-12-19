def print_line(number):
    print(*[num for num in range(1, number+1)], sep='')


def triangle_maker(number):
    for r in range(1, number + 1):
        print_line(r)

    for r in range(number - 1, 0, -1):
        print_line(r)


def square_maker(number):
    for _ in range(1, 1+number):
        print_line(number)


def math_ops(first_number, second_number, operator):
    if operator == '+':
        result = first_number + second_number

    elif operator == '-':
        result = first_number - second_number

    elif operator == '*':
        result = first_number * second_number

    elif operator == '/':
        result = first_number / second_number

    elif operator == '^':
        result = first_number ** second_number

    print(f"{result:.2f}")


def create_fibonacci_seq(number):
    nums_list = []
    if number == 0:
        nums_list = []
    elif number == 1:
        nums_list = [0]
    else:
        nums_list = [0, 1]
        for _ in range(2, number):
            nums_list.append(nums_list[-1] + nums_list[-2])
    return nums_list


def locate_in_seq(current_list, number):
    if number not in current_list:
        idx = -1
    else:
        idx = current_list.index(number)
    return idx