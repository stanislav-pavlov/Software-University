N = int(input())

matrix = [[x] for x in input().split() for _ in range(N)]

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == "K":
            if row >= 2 and col >= 2:
                pass
            elif row
