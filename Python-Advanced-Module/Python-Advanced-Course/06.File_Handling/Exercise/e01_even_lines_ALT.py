with open("e01_text.txt", 'r') as file:
    replace_chars = ["-", ",", ".", "!", "?"]
    text = file.readlines()

    for line in range(0, len(text), 2):
        for sym in replace_chars:
            text[line] = text[line].replace(sym, '@')
        print(*text[line].split()[::-1])