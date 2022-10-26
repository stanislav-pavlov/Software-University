import re

text = input()
pattern = r"([=/])([A-Z][A-Za-z]{2,})\1"

destinations = []
points = 0

matches = re.finditer(pattern, text)

for match in matches:
    destinations.append(match[2])
    points += len(match[2])

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel points: {points}")