rows, columns = tuple(map(int, input().split()))
matrix = []
max_sum = -1
three_by_three_square_matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for r in range(rows-2):
    for c in range(columns-2):
        current_sum = matrix[r][c] + matrix[r][c+1] + matrix[r][c+2] +\
                      matrix[r+1][c] + matrix[r+1][c+1] + matrix[r+1][c+2] + \
                      matrix[r+2][c] + matrix[r+2][c+1] + matrix[r+2][c+2]
        if current_sum > max_sum:
            max_sum = current_sum
            three_by_three_square_matrix = [
                [matrix[r][c], matrix[r][c+1], matrix[r][c+2]],
                [matrix[r+1][c], matrix[r+1][c+1], matrix[r+1][c+2]],
                [matrix[r+2][c], matrix[r+2][c+1], matrix[r+2][c+2]]
            ]

print(f"Sum = {max_sum}")
for row in three_by_three_square_matrix:
    print(' '.join(list(map(str, row))))