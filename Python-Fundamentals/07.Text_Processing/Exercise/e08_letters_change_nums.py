from string import ascii_lowercase


def extract_num(text):
    current_nums_list = [num for num in text if num.isdigit()]
    current_num = int(''.join(current_nums_list))
    result = 0

    for i in range(len(text)):
        if text[i].isalpha():
            index = ascii_lowercase.index(text[i].lower()) + 1

            if i == 0:
                if text[i] == text[i].lower():
                    result = index * current_num
                else:
                    result = current_num / index
            else:
                if text[i] == text[i].lower():
                    result += index
                else:
                    result -= index

    return result


def letters_change_nums(data):
    result = 0
    for element in data:
        result += extract_num(element)

    print(f"{result:.2f}")


line = input().split()
letters_change_nums(line)