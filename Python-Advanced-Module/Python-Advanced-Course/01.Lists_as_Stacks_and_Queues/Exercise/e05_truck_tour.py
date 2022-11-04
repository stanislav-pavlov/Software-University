from collections import deque

N = int(input())
petrol_loads = deque([])
distances = deque([])
pumps = deque([])
fuel_in_tank = 0
first_pump = []

for i in range(N):
    current_pump_data = input().split()
    petrol_from_current_pump = int(current_pump_data[0])
    distance_to_next_pump = int(current_pump_data[1])
    petrol_loads.append(petrol_from_current_pump)
    distances.append(distance_to_next_pump)
    pumps.append(i)

while len(first_pump) <= N:
    fuel_in_tank += petrol_loads[0]
    if fuel_in_tank >= distances[0]:
        first_pump.append(pumps[0])
        fuel_in_tank -= distances[0]
        petrol_loads.append(petrol_loads.popleft())
        distances.append(distances.popleft())
        pumps.append(pumps.popleft())

    else:
        fuel_in_tank = 0
        petrol_loads.append(petrol_loads.popleft())
        distances.append(distances.popleft())
        pumps.append(pumps.popleft())
        first_pump.clear()

print(first_pump[0])