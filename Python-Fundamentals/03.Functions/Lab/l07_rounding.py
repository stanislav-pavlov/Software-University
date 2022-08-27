initial_list = input().split(" ")
final_list = list()

for x in initial_list:
    rounded_num = round(float(x))
    final_list.append(rounded_num)

print(final_list)