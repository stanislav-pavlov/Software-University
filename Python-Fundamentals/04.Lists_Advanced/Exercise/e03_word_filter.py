def word_filter(words_list):
    even_length_words = [word for word in words_list if len(word) % 2 == 0]
    print("\n".join(even_length_words))


initial_list = input().split(" ")
word_filter(initial_list)