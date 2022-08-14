n = int(input())
keyword = input()
all_str = list()
keyw_list = list()

for i in range(n):
    all_str.append(input())

for current_str in all_str:
    if keyword in current_str:
        keyw_list.append(current_str)

print(all_str)
print(keyw_list)