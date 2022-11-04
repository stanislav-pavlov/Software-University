parentheses = input()
stack = []
balanced = True

for p in parentheses:
    if p in ['(', '[', '{']:
        stack.append(p)
    if stack:
        if p == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                balanced = False
                break
        elif p == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                balanced = False
                break
        elif p == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                balanced = False
                break
    else:
        balanced = False

if balanced:
    print("YES")
else:
    print("NO")