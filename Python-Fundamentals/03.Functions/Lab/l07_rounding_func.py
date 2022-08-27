def convert_to_round_list(initial_list):
    final_list = list()

    for x in initial_list:
        rounded_num = round(float(x))
        final_list.append(rounded_num)
    return final_list


initial_list_input = input().split(" ")
print(convert_to_round_list(initial_list_input))