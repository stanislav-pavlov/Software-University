from functools import reduce

str_exp = input().split()
nums_stack = []

for sym in str_exp:
    if sym.lstrip('-').isdigit():
        nums_stack.append(int(sym))
    elif sym == '+':
        nums_stack = [reduce(lambda x, y: x + y, nums_stack)]
    elif sym == '-':
        nums_stack = [reduce(lambda x, y: x - y, nums_stack)]
    elif sym == '*':
        nums_stack = [reduce(lambda x, y: x * y, nums_stack)]
    elif sym == '/':
        nums_stack = [reduce(lambda x, y: x // y, nums_stack)]

print(nums_stack[0])

#can be solved with queue