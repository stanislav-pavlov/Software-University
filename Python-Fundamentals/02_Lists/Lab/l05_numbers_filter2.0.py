num = int(input())
numbers = list()

even = list()
odd = list()
positive = list()
negative = list()

for i in range(num):
    current_num = int(input())
    numbers.append(current_num)

filter_word = input()

for current_num in numbers:
    if filter_word == "positive" and current_num >= 0:
        positive.append(current_num)
    if filter_word == "negative" and current_num < 0:
        negative.append(current_num)
    if filter_word == "even" and (current_num % 2 == 0 or current_num == 0):
        even.append(current_num)
    if filter_word == "odd" and current_num % 2 != 0:
        odd.append(current_num)

print(eval(filter_word))