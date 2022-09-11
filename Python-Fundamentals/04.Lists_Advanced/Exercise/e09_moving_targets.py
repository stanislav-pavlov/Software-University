def target_manipulation(seq):
    cmd = input()

    while cmd != "End":
        cmd_elements = cmd.split(' ')
        current_cmd = cmd_elements[0]
        index = int(cmd_elements[1])
        pwr_val_rad = int(cmd_elements[2])

        if current_cmd == "Shoot" and index < len(seq):
            single_value = seq.pop(index)
            updated_value = single_value - pwr_val_rad
            if updated_value > 0:
                seq.insert(index, updated_value)

        elif current_cmd == "Add":
            if index < len(seq):
                seq.insert(index, pwr_val_rad)
            else:
                print("Invalid placement!")

        elif current_cmd == "Strike":
            preceding_index = int(index - pwr_val_rad)
            sequential_index = int(index + pwr_val_rad)
            if 0 <= preceding_index and sequential_index <= len(seq):
                del seq[preceding_index:sequential_index + 1]
            else:
                print("Strike missed!")

        cmd = input()

    print('|'.join(map(str, seq)))


target_sequence = list(map(int, input().split(' ')))
target_manipulation(target_sequence)