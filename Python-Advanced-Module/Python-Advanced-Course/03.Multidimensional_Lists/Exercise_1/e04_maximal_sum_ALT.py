rows, columns = tuple(map(int, input().split()))
matrix = []
max_sum = -1
three_by_three_square_matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for r in range(rows-2):
    for c in range(columns-2):
        temp_matrix = [
                [matrix[r][c], matrix[r][c+1], matrix[r][c+2]],
                [matrix[r+1][c], matrix[r+1][c+1], matrix[r+1][c+2]],
                [matrix[r+2][c], matrix[r+2][c+1], matrix[r+2][c+2]]
            ]
        sum_temp_matrix = sum(sum(temp_matrix, []))
        if sum_temp_matrix > max_sum:
            max_sum = sum_temp_matrix
            three_by_three_square_matrix = temp_matrix

print(f"Sum = {max_sum}")
for row in three_by_three_square_matrix:
    print(' '.join(map(str, row)))