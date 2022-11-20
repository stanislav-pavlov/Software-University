rows = int(input())
matrix = [input().split() for row in range(rows)]
primary_diagonal = []
secondary_diagonal = []

for idx in range(rows):
    primary_diagonal.append(matrix[idx][idx])
    secondary_diagonal.append(matrix[idx][rows - idx - 1])

print(abs((sum(map(int, primary_diagonal))) - (sum(map(int, secondary_diagonal)))))