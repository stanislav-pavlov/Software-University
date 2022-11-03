from collections import deque

food_quantity = int(input())

orders = deque(map(int, input().split()))
print(max(orders))

while len(orders) >= 1:
    if food_quantity >= orders[0]:
        food_quantity -= orders.popleft()
    else:
        break

if len(orders) == 0:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(map(str, orders))}")