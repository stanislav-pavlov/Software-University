import re

user_pattern = r"( |^)[a-zA-Z0-9]+([\.|\-|\_][a-zA-Z0-9]+)*"
host_pattern = r"[a-zA-Z]+(\-?[a-z]+)*(\.[a-z]+)+"

full_pattern = rf"{user_pattern}@{host_pattern}"

text = input()

emails = re.finditer(full_pattern, text)

for email in emails:
    print(email[0])
