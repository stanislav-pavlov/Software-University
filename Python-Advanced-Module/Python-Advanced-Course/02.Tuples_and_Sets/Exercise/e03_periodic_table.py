count = int(input())
periodic_table = set()

for _ in range(count):
    line = input().split()
    for el in line:
        periodic_table.add(el)

[print(x) for x in periodic_table]