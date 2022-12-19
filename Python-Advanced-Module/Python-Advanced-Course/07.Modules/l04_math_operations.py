from Custom_Modules.custom_funcs import math_ops

line = input().split()

num1 = float(line[0])
num2 = int(line[2])
operator = line[1]

math_ops(num1, num2, operator)