from math import log, e

number = int(input())
base_input = input()

base = e if base_input == "natural" else int(base_input)

print(f"{log(number, base):.2f}")
