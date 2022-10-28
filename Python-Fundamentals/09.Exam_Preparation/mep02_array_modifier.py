int_array = list(map(int, input().split(" ")))
cmd = input()

while cmd != "end":
    if cmd == "decrease":
        int_array = list(map(lambda num: num -1, int_array))
    else:
        cmd_elements = cmd.split(" ")
        action = cmd_elements[0]
        index1 = int(cmd_elements[1])
        index2 = int(cmd_elements[2])

        if action == "swap":
            int_array[index1], int_array[index2] = int_array[index2], int_array[index1]

        elif action == "multiply":
            int_array[index1] = int_array[index1] * int_array[index2]

    cmd = input()

print(", ".join(map(str, int_array)))