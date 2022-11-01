from collections import deque

total_water = int(input())
wanna_be_drinkers_q = deque([])

line = input()
while line != "Start":
    wanna_be_drinkers_q.append(line)
    line = input()

line = input()
while line != "End":
    if "refill" in line:
        line = line.split()
        total_water += int(line[1])
    else:
        desired_liters = int(line)
        if total_water >= desired_liters:
            print(f"{wanna_be_drinkers_q.popleft()} got water")
            total_water -= desired_liters
        else:
            print(f"{wanna_be_drinkers_q.popleft()} must wait")

    line = input()

print(f"{total_water} liters left")