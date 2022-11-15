from collections import deque

strings = deque(input().split())
all_colors = []
MAIN_COLORS = ['red', 'yellow', 'blue']
SECONDARY_COLORS = ['orange', 'purple', 'green']

while strings:
    first_str = strings.popleft()
    if strings:
        last_str = strings.pop()
    else:
        last_str = ''
    substring = first_str + last_str
    substring_2 = last_str + first_str
    if substring in MAIN_COLORS or substring in SECONDARY_COLORS:
        all_colors.append(substring)
    elif substring_2 in MAIN_COLORS or substring_2 in SECONDARY_COLORS:
        all_colors.append(substring_2)
    else:
        first_stripped = first_str[:-1]
        last_stripped = last_str[:-1]
        idx = len(strings) // 2
        if first_stripped:
            strings.insert(idx, first_stripped)
        if last_stripped:
            strings.insert(idx, last_stripped)

if "orange" in all_colors and ("red" not in all_colors or "yellow" not in all_colors or ("red" not in all_colors and "yellow" not in all_colors)):
    all_colors.remove("orange")
if "purple" in all_colors and ("red" not in all_colors or "blue" not in all_colors or ("red" not in all_colors and "blue" not in all_colors)):
    all_colors.remove("purple")
if "green" in all_colors and ("yellow" not in all_colors or "blue" not in all_colors or ("yellow" not in all_colors and "blue" not in all_colors)):
    all_colors.remove("green")

print(all_colors)