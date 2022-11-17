rows, columns = tuple(map(int, input().split(', ')))
matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for col in range(columns):
    total_sum = 0
    for row in range(rows):
        total_sum += matrix[row][col]
    print(total_sum)