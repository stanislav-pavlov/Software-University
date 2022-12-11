import string

output_file = open("e02_output.txt", 'a')

with open("e01_text.txt", 'r') as text_file:
    text = text_file.readlines()
    for row in range(len(text)):
        letters_count = 0
        punctuation_marks_count = 0

        for ch in text[row]:
            if ch in string.ascii_letters:
                letters_count += 1
            elif ch in string.punctuation:
                punctuation_marks_count += 1

        output_file.write(f"Line {row+1}: {text[row][:-1]} ({letters_count})({punctuation_marks_count})\n")


output_file.close()