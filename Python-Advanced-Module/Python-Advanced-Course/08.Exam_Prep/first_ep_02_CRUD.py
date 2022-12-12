rows, columns = 6, 6
matrix = []
for r in range(rows):
    line = input().split()
    matrix.append(line)

first_pos = input()
row = int(first_pos[1])
col = int(first_pos[4])

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

cmd = input()
while cmd != "Stop":
    cmd = cmd.split(', ')
    command = cmd[0]
    dir = cmd[1]

    row += directions[dir][0]
    col += directions[dir][1]

    if matrix[row][col] == '.':
        if command == "Create":
            value = cmd[2]
            matrix[row][col] = value
    elif matrix[row][col] != '.':
        if command == "Update":
            value = cmd[2]
            matrix[row][col] = value
        elif command == "Delete":
            matrix[row][col] = '.'
        elif command == "Read":
            print(matrix[row][col])

    cmd = input()

for r in matrix:
    print(' '.join(r))
