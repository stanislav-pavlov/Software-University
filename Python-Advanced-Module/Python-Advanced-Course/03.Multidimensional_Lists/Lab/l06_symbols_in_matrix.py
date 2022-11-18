size = int(input())
matrix = []

for _ in range(size):
    matrix.append([x for x in input()])
target_char = input()
found = False
found_in_row = 0
found_in_col = 0
for row in range(size):
    for col in range(size):
        if matrix[row][col] == target_char:
            found = True
            found_in_row = row
            found_in_col = col
            break
    if found:
        break
if found:
    print(f"({found_in_row}, {found_in_col})")
else:
    print(f"{target_char} does not occur in the matrix")