n = int(input())
stack = []

for _ in range(n):
    line = input()

    if '1' in line:
        line = line.split()
        number_to_push = int(line[1])
        stack.append(number_to_push)
    elif line == '2' and len(stack) > 0:
        stack.pop()
    elif line == '3' and len(stack) > 0:
        print(max(stack))
    elif line == '4' and len(stack) > 0:
        print(min(stack))

for _ in range(len(stack)):
    if len(stack) <= 1:
        print(stack.pop())
    else:
        print(stack.pop(), end=', ')