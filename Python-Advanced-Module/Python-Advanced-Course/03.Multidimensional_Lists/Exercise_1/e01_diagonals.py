size = int(input())
matrix = []
primary_diagonal_list = []
secondary_diagonal_list = []

for _ in range(size):
    matrix.append([int(x) for x in input().split(', ')])

# for idx in range(size):
#     primary_diagonal_list.append(matrix[idx][idx])
#     primary_diagonal_sum += matrix[idx][idx]

for row in range(size):
    for col in range(size):
        if row == col:
            primary_diagonal_list.append(matrix[row][col])
        if row + col == size - 1:
            secondary_diagonal_list.append(matrix[row][col])

print(f"Primary diagonal: {', '.join(map(str, primary_diagonal_list))}. Sum: {sum(primary_diagonal_list)}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal_list))}. Sum: {sum(secondary_diagonal_list)}")