import re

regex = r"\b_[a-zA-Z0-9]+\b"
text = input()

result = re.findall(regex, text)

print(','.join(result).replace('_', ''))