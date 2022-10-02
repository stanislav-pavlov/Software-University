def sum_func(longer_str, shorter_str):
    total_sum = 0
    for i in range(len(longer_str)):
        if i < len(shorter_str):
            total_sum += ord(longer_str[i]) * ord(shorter_str[i])
        else:
            total_sum += ord(longer_str[i])
    return total_sum


def char_multiplier(first_str, second_str):
    result = 0

    if len(first_str) > len(second_str):
        result = sum_func(first_str, second_str)
    else:
        result = sum_func(second_str, first_str)

    print(result)


line = input().split()
char_multiplier(line[0], line[1])
