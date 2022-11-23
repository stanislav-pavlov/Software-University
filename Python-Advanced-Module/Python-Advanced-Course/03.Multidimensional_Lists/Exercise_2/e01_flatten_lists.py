line = input().split('|')

list_to_print = []

for el in line[::-1]:
    list_to_print.extend(el.split())

print(*list_to_print)