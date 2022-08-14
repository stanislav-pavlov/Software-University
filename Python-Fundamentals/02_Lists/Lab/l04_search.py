n = int(input())
keyword = input()
all_str_list = list()
keyw_list = list()

for i in range(n):
    current_str = input()
    all_str_list.append(current_str)
    if keyword in current_str:
        keyw_list.append(current_str)

print(all_str_list)
print(keyw_list)