num = int(input())
numbers = list()

for i in range(num):
    current_num = int(input())
    numbers.append(current_num)

filter_word = input()
filtered = list()

for current_num in numbers:
    if filter_word == "positive" and current_num >= 0:
        filtered.append(current_num)
    if filter_word == "negative" and current_num < 0:
        filtered.append(current_num)
    if filter_word == "even" and (current_num % 2 == 0 or current_num == 0):
        filtered.append(current_num)
    if filter_word == "odd" and current_num % 2 != 0:
        filtered.append(current_num)

print(filtered)