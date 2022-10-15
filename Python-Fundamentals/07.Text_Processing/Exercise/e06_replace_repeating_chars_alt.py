def replace_chars(data):
    new_list = []

    for i in range(len(data)-1):
        if data[i] != data[i+1]:
            new_list.append(data[i])

    new_list.append(data[len(data)-1])

    print(''.join(new_list))


line = input()
replace_chars(line)