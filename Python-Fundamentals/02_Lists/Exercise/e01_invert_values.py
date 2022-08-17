# numbers = input().split(' ') #string
# ints_list = []
#
# for num in numbers:
#     ints_list.append(int(num) * -1)
#
# print(ints_list)

ints_list = [num * -1 for num in list(map(int, input().split(' ')))]
print(ints_list)