# https://judge.softuni.org/Contests/Practice/Index/2303#1
import re

count = int(input())
pattern = r"@#+[A-Z][A-Za-z0-9]+[A-Z]@#+"
digits_pattern = r"\d"

for i in range(count):
    barcode = input()
    result = re.findall(pattern, barcode)

    if len(''.join(result)) >= 10:
        digits = re.findall(digits_pattern, ''.join(result))
        if len(digits) > 0:
            concatenated_digits = ''.join(digits)
            print(f"Product group: {concatenated_digits}")
        else:
            print(f"Product group: 00")
    else:
        print("Invalid barcode")