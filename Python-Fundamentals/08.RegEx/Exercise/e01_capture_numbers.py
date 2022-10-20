import re

regex = r"\d+"

while True:
    text = input()

    if not text:
        break

    result = re.findall(regex, text)

    if len(result) > 0:
        print(f"{' '.join(result)}", end=' ')