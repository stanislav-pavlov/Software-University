with open("e01_text.txt", 'r') as file:
    replace_chars = ["-", ",", ".", "!", "?"]

    text = file.readlines()

    for i in range(len(text)):
        if i % 2 == 0:
            for ch in text[i]:
                if ch in replace_chars:
                    text[i] = text[i].replace(ch, '@')

            for word in text[i].split()[::-1]:
                print(word, end=' ')
            print()
