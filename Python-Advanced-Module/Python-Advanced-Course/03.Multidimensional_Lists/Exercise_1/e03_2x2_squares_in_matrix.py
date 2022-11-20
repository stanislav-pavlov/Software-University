rows, columns = tuple(map(int, input().split()))
matrix = []
square_matrices_count = 0

for _ in range(rows):
    matrix.append([x for x in input().split()])

for r in range(rows-1):
    for c in range(columns-1):
        if matrix[r][c] == matrix[r][c+1] == matrix[r+1][c] == matrix[r+1][c+1]:
            square_matrices_count += 1

print(square_matrices_count)