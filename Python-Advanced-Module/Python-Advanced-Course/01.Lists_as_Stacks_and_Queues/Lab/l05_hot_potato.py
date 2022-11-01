from collections import deque

names = deque(input().split())
n = int(input())
counter = 1

while len(names) > 1:
    kid = names.popleft()
    if counter == n:
        print(f"Removed {kid}")
        counter = 1
    else:
        counter += 1
        names.append(kid)

last_kid = names.popleft()
print(f"Last is {last_kid}")