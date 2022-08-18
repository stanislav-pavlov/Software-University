factor = int(input())
count = int(input())
new_list = []

for i in range(1, count+1):
    new_list.append(factor * i)

print(new_list)