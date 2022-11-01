text = input()
stack = []

for i in range(len(text)):
    current_index = i
    if text[i] == '(':
        stack.append(i)
    elif text[i] == ')':
        latest_opening_bracket = stack.pop()
        print(text[latest_opening_bracket:i+1])