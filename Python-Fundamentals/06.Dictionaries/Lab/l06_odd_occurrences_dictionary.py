word_sequence = input().lower().split(' ')
my_dictionary = {}

for word in word_sequence:
    if word not in my_dictionary.keys():
        my_dictionary[word] = 1
    else:
        my_dictionary[word] += 1

for word in my_dictionary.keys():
    if my_dictionary[word] % 2 != 0:
        print(f"{word}", end=' ')