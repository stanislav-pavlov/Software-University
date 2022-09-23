line = input().replace(' ','')
dictionary = {}

for ch in line:
    if ch not in dictionary.keys():
        dictionary[ch] = 1
    else:
        dictionary[ch] += 1

for key, value in dictionary.items():
    print(f"{key} -> {value}")