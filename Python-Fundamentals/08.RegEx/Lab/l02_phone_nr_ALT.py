import re
phone_nums = input()
regex = r"\+359([ -])2\1\d{3}\1\d{4}\b"
matches = re.finditer(regex, phone_nums)
final_output = []

for match in matches:
    final_output.append(match.group())

print(', '.join(final_output))