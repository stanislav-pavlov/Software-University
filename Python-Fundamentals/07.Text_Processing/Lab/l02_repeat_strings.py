line = input().split()

for word in line:
    print(f"{word * len(word)}", end='')