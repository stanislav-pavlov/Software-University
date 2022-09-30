line = input()

while line != "end":
    rev = reversed(line)
    new_text = ''.join(rev)
    print(f"{line} = {new_text}")
    line = input()