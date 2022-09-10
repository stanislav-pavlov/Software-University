initial_list = input().split(" ")
deciphered = []

for word in initial_list:
    ascii_char = [char for char in word if char.isdigit()]
    word_chars_list = [char for char in word if char not in ascii_char]

    first_letter = chr(int("".join(ascii_char)))
    word_chars_list[0], word_chars_list[-1] = word_chars_list[-1], word_chars_list[0]
    new_word = first_letter + ''.join(word_chars_list)
    deciphered.append(new_word)

print(' '.join(deciphered))