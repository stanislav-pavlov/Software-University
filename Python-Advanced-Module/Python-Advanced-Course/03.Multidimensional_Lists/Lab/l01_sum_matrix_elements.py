rows, columns = tuple(map(int, input().split(', ')))
matrix = []

total_sum = 0

for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

for row in range(rows):
    for col in range(columns):
        total_sum += matrix[row][col]

print(total_sum)
print(matrix)