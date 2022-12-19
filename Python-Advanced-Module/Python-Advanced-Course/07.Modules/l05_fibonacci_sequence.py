from Custom_Modules.custom_funcs import create_fibonacci_seq, locate_in_seq

line = input()
nums_list = [0]


while line != "Stop":
    cmd = line.split()
    command = cmd[0]
    if command == "Create":
        num = int(cmd[2])
        print(*create_fibonacci_seq(num))
    elif command == "Locate":
        num = int(cmd[1])
        idx = locate_in_seq(create_fibonacci_seq(num), num)
        if idx >= 0:
            print(f"The number - {num} is at index {idx}")
        else:
            print(f"The number {num} is not in the sequence")

    line = input()
#   0 1 1 2 3 5 8 13 21 34