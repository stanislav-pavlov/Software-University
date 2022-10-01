line = input()

[print(f"{ch}", end='') for ch in line if ch.isdigit()]
print('')
[print(f"{ch}", end='') for ch in line if ch.isalpha()]
print('')
[print(f"{ch}", end='') for ch in line if not ch.isdigit() and not ch.isalpha()]