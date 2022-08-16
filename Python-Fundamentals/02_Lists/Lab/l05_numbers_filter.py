numbers = int(input())
even = list()
odd = list()
positive = list()
negative = list()


for i in range(numbers):
    current_num = int(input())
    if current_num >= 0:
        positive.append(current_num)
    else:
        negative.append(current_num)

    if current_num % 2 == 0 or current_num == 0:
        even.append(current_num)
    else:
        odd.append(current_num)

filter_word = input()

if filter_word == "even":
    print(even)
elif filter_word == "odd":
    print(odd)
elif filter_word == "positive":
    print(positive)
elif filter_word == "negative":
    print(negative)