size = int(input())
matrix = []

for _ in range(size):
    matrix.append([(int(x)) for x in input().split(', ')])

flattened_matrix = [x for sublist in matrix for x in sublist]
print(matrix)
print(flattened_matrix)