# def abs_value():
#

initial_list = input().split(" ")
abs_list = list()

for n in initial_list:
    current_abs = abs(float(n))
    abs_list.append(current_abs)

print(abs_list)