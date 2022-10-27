import re

line = input()
pattern = r"([|#])([a-zA-Z ]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1"
items = []

result = re.findall(pattern, line)

for item in result:
    current_item = [el for el in item if el != "#" and el != "|"]
    items.append(current_item)

total_calories = 0

for item in items:
    calories = int(item[2])
    total_calories += calories

days_ensured = int(total_calories / 2000)
print(f"You have food to last you for: {days_ensured} days!")

for item in items:
    food = item[0]
    bb = item[1]
    cal = item[2]
    print(f"Item: {food}, Best before: {bb}, Nutrition: {cal}")