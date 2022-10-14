def replace_chars(data):
    char_list = list(data)
    i = 1
    while i < len(char_list):
        if char_list[i] == char_list[i-1]:
            char_list.pop(i)
            i -= 1
        i += 1

    print(''.join(char_list))


line = input()
replace_chars(line)