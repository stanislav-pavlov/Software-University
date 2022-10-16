data = input()
my_string = []
multiplier_digits_list = []
unique_symbols_list = []
spam_to_print = []

for i in range(len(data)):
    if data[i].isdigit():
        multiplier_digits_list.append(data[i])

        if i != len(data) - 1 and data[i+1].isdigit():
            continue
        else:
            multiplier = int(''.join(multiplier_digits_list))
            spam_to_print.append(''.join(my_string) * multiplier)
            my_string.clear()
            multiplier_digits_list.clear()
    else:
        my_string.append(data[i].upper())
        if data[i].upper() not in unique_symbols_list:
            unique_symbols_list.append(data[i].upper())

print(f"Unique symbols used: {len(unique_symbols_list)}")
print(f"{''.join(spam_to_print)}")
