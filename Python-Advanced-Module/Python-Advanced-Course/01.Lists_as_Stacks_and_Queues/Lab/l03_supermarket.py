from collections import deque

q = deque([])
line = input()

while line != "End":
    if line == "Paid":
        while len(q) > 0:
            print(q.popleft())
    else:
        q.append(line)

    line = input()

print(f"{len(q)} people remaining.")