word_sequence = input().lower().split(' ')
new_list = []

for word in word_sequence:
    if word_sequence.count(word) % 2 != 0 and word not in new_list:
        new_list.append(word)

print(' '.join(new_list))