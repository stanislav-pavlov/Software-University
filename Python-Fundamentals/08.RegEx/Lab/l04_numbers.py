import re

initial_string = input()
regex = r"(^|(?<=\s))-?([0]|[1-9]\d*)(\.\d+)?(($|(?=\s)))"
matches = re.finditer(regex, initial_string)
final_output = []

for match in matches:
    final_output.append(match.group())

print(' '.join(final_output))