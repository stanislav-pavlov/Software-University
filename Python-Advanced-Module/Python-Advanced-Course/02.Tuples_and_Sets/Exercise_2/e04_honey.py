from collections import deque

working_bees_q = deque(map(int, input().split()))
nectar_stack = list(map(int, input().split()))
operators = deque(input().split())
total_honey = 0

while working_bees_q and nectar_stack:
    if nectar_stack[-1] >= working_bees_q[0]:
        bee = working_bees_q.popleft()
        collected_nectar = nectar_stack.pop()
        symbol = operators.popleft()
        if symbol == "+":
            total_honey += abs(bee + collected_nectar)
        elif symbol == '-':
            total_honey += abs(bee - collected_nectar)
        elif symbol == '*':
            total_honey += abs(bee * collected_nectar)
        elif symbol == '/':
            if collected_nectar == 0 or bee == 0:
                continue
            total_honey += abs(bee / collected_nectar)
    else:
        nectar_stack.pop()

print(f"Total honey made: {total_honey}")
if working_bees_q:
    print(f"Bees left: {', '.join(map(str, working_bees_q))}")
if nectar_stack:
    print(f"Nectar left: {', '.join(map(str, nectar_stack))}")