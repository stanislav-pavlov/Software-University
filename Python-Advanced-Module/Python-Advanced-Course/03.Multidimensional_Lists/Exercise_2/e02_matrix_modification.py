size = int(input())
matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

command = input()
while command != "END":
    cmd = command.split()
    if 0 <= int(cmd[1]) < len(matrix) and 0 <= int(cmd[2]) < len(matrix):
        target_row = int(cmd[1])
        target_col = int(cmd[2])
        val = int(cmd[3])

        if cmd[0] == "Add":
            matrix[target_row][target_col] += val
        elif cmd[0] == "Subtract":
            matrix[target_row][target_col] -= val
    else:
        print("Invalid coordinates")

    command = input()

[print(*row) for row in matrix]

# for row in matrix:
#     print(*row)