from collections import deque

available_seats = input().split(', ')
first_num_list = deque(map(int, input().split(', ')))
last_num_list = list(map(int, input().split(', ')))

rotations_count = 0
taken_seats = []

while rotations_count < 10 and len(taken_seats) < 3:
    nums_sum = first_num_list[0] + last_num_list[-1]
    ascii_char = chr(nums_sum)
    target_seats = [str(first_num_list[0]) + ascii_char, str(last_num_list[-1]) + ascii_char]
    rotations_count += 1
    found_match = False

    for free_seat in available_seats:
        for searched_seat in target_seats:
            if searched_seat == free_seat:
                taken_seats.append(searched_seat)
                idx = available_seats.index(free_seat)
                available_seats.pop(idx)
                found_match = True
                break

        if found_match:
            break

    if found_match:
        first_num_list.popleft()
        last_num_list.pop()
    else:
        first_num_list.append(first_num_list.popleft())
        last_num_list = last_num_list[-1:] + last_num_list[:-1]

print(f"Seat matches: {', '.join(taken_seats)}")
print(f"Rotations count: {rotations_count}")