def explosion(my_str):
    new_str = ''
    expl_pwr = 0

    for i in range(len(my_str)):
        if my_str[i] == '>':
            expl_pwr += int(my_str[i+1])
            new_str += my_str[i]
        elif my_str[i] != '>' and expl_pwr > 0:
            expl_pwr -= 1
        else:
            new_str += my_str[i]

    print(new_str)


line = input()
explosion(line)