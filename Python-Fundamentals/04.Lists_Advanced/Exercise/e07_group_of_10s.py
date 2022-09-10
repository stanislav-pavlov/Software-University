numbers = list(map(int, input().split(", ")))
upper_boundary = 10
max_num = max(numbers)

while len(numbers) > 0:
    new_list = list(filter(lambda x: x <= upper_boundary, numbers))
    print(f"Group of {upper_boundary}'s: {new_list}")

    numbers = list(filter(lambda x: x > upper_boundary, numbers))
    # print(numbers)
    # max_num = max(numbers)

    upper_boundary += 10