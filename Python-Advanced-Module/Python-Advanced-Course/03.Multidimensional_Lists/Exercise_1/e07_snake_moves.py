rows, columns = tuple(map(int, input().split()))
snake = input()

matrix = []
idx = 0

for r in range(rows):
    result = ''
    for c in range(columns):
        result += snake[idx % len(snake)]
        idx += 1

    if r % 2 == 0 or r == 0:
        matrix.append(result)
    else:
        matrix.append(result[::-1])

for row in matrix:
    print(*row, sep='')