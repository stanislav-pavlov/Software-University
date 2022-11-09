N = int(input())
parked_cars = set()

for _ in range(N):
    line = tuple(input().split(', '))
    direction, plate = line

    if direction == "IN":
        parked_cars.add(plate)
    elif direction == "OUT":
        parked_cars.remove(plate)

if parked_cars:
    for plate in parked_cars:
        print(plate)
else:
    print("Parking Lot is Empty")