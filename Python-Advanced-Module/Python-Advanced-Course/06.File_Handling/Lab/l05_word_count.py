import re

words_dict = {}
pattern = r"[A-Za-z'\*]+"
with open("words.txt", 'r') as words_file:
    all_words = words_file.read().split()
    words_dict = {word.lower(): 0 for word in all_words}

with open("text.txt", 'r') as text_file:
    for line in text_file:
        words_in_current_line = re.findall(pattern, line)
        for word in words_in_current_line:
            word_lower = word.lower()
            if word_lower in words_dict:
                words_dict[word_lower] += 1

with open("output.txt", 'w') as final_file:
    for key, value in sorted(words_dict.items(), key=lambda x: -x[1]):
        final_file.write(f"{key} - {value}\n")