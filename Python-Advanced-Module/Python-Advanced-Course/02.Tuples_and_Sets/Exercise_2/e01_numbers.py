sequence1 = map(int, input().split())
set1 = set()
for num in sequence1:
    set1.add(num)

sequence2 = map(int, input().split())
set2 = set()
for num in sequence2:
    set2.add(num)

N = int(input())

for _ in range(N):
    line = input().split()
    if "Add" in line:
        if "First" in line:
            for i in range(2, len(line)):
                set1.add(int(line[i]))
        elif "Second" in line:
            for i in range(2, len(line)):
                set2.add(int(line[i]))
    elif "Remove" in line:
        if "First" in line:
            for i in range(2, len(line)):
                if int(line[i]) in set1:
                    set1.remove(int(line[i]))
        elif "Second" in line:
            for i in range(2, len(line)):
                if int(line[i]) in set2:
                    set2.remove(int(line[i]))
    elif "Check" in line and "Subset" in line:
        if set1 < set2 or set2 < set1:
            print("True")
        else:
            print("False")

print(f"{sorted(set1)}".replace('[','').replace(']',''))
print(f"{sorted(set2)}".replace('[','').replace(']',''))

# print(f"{str(sorted(set1)).replace('[', '').replace(']', '')}")
# print(f"{str(sorted(set2)).replace('[', '').replace(']', '')}")
