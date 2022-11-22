rows, columns = tuple(map(int, input().split()))
matrix = []

for _ in range(rows):
    matrix.append([x for x in input().split()])

command = input()
while command != "END":
    command = command.split()
    if "swap" not in command or len(command) != 5:
        print("Invalid input!")
        command = input()
        continue
    else:
        first_pair_row = int(command[1])
        first_pair_col = int(command[2])
        second_pair_row = int(command[3])
        second_pair_col = int(command[4])

        if 0 <= first_pair_row < rows and \
                0 <= first_pair_col < columns and \
                0 <= second_pair_row < rows and \
                0 <= second_pair_col < columns:
            val_1 = matrix[first_pair_row][first_pair_col]
            val_2 = matrix[second_pair_row][second_pair_col]

            matrix[first_pair_row][first_pair_col] = val_2
            matrix[second_pair_row][second_pair_col] = val_1

            for row in matrix:
                print(' '.join(map(str, row)))
        else:
            print("Invalid input!")
            command = input()
            continue

    command = input()
