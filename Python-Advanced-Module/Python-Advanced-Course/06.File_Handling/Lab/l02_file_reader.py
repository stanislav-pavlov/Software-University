file_path = "numbers.txt"
nums_sum = 0

file = open(file_path, "r")
for num in file:
    nums_sum += int(num)

print(nums_sum)