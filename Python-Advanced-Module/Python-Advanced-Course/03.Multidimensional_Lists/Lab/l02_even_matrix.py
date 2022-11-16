size = int(input())
result = []

for _ in range(size):
    result.append([(int(x)) for x in input().split(', ') if int(x) % 2 == 0])

print(result)