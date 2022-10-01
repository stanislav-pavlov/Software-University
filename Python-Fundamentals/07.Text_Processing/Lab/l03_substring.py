searched_str = input()
full_str = input()

while searched_str in full_str:
    full_str = full_str.replace(searched_str, '')

print(full_str)