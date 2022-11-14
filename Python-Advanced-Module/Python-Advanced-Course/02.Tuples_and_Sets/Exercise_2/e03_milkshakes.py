from collections import deque

chocolates_stack = list(map(int, input().split(', ')))
milk_q = deque(map(int, input().split(', ')))
milkshakes = 0
success = False

while milkshakes < 5 and chocolates_stack and milk_q:
    flag = False
    if chocolates_stack[-1] <= 0:
        chocolates_stack.pop()
        flag = True
    if milk_q[0] <= 0:
        milk_q.popleft()
        flag = True
    if flag:
        continue

    if chocolates_stack[-1] == milk_q[0]:
        milkshakes += 1
        chocolates_stack.pop()
        milk_q.popleft()
        if milkshakes == 5:
            success = True
            break
    else:
        milk_q.append(milk_q.popleft())
        chocolates_stack[-1] -= 5

if success:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates_stack:
    print(f"Chocolate: {', '.join(map(str, chocolates_stack))}")
else:
    print("Chocolate: empty")

if milk_q:
    print(f"Milk: {', '.join(map(str, milk_q))}")
else:
    print("Milk: empty")