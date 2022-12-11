import os

directory = input()

extensions_dict = {}

for filename in os.listdir(directory):
    file = os.path.join(directory, filename)

    if os.path.isfile:
        extension = filename.split('.')[1]
        if extension not in extensions_dict:
            extensions_dict[extension] = []
        else:
            extensions_dict[extension].append(filename)

for key, value in sorted(extensions_dict.items()):
    print(f".{key}")
    for v in value:
        print(f"--- {v}")