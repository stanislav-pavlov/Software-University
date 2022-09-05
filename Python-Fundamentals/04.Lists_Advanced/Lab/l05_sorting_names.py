names_list = input().split(", ")

sorted_names = sorted(names_list)
sorted_names = sorted(sorted_names, key=lambda x: (-len(x), x))

print(sorted_names)