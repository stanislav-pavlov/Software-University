clothes_stack = list(map(int, input().split()))
rack_capacity = int(input())
rack_counter = 1
capacity_left_current_rack = rack_capacity

while clothes_stack:
    if clothes_stack[-1] <= capacity_left_current_rack:
        capacity_left_current_rack -= clothes_stack.pop()
    else:
        rack_counter += 1
        capacity_left_current_rack = rack_capacity
        capacity_left_current_rack -= clothes_stack.pop()

print(rack_counter)