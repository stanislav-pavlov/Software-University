sequence1 = input().split(", ")
full_string = input()

new_list = [word for word in sequence1 if word in full_string]
print(new_list)