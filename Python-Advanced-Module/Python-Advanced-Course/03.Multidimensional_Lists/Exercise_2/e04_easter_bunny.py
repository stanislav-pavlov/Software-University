size = int(input())
field = []

bunny_pos = []
best_path = []
best_direction = None
max_collected_eggs = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
for r in range(size):
    line = input().split()
    if "B" in line:
        bunny_pos = [r, line.index("B")]
    field.append(line)

for direction, positions in directions.items():
    row = bunny_pos[0] + positions[0]
    col = bunny_pos[1] + positions[1]

    path = []
    collected_eggs = 0

    while 0 <= row < size and 0 <= col < size:
        if field[row][col] == "X":
            break

        collected_eggs += int(field[row][col])
        path.append([row, col])

        row += positions[0]
        col += positions[1]

    if collected_eggs >= max_collected_eggs:
        max_collected_eggs = collected_eggs
        best_direction = direction
        best_path = path

print(best_direction)
print(*best_path, sep='\n')
print(max_collected_eggs)