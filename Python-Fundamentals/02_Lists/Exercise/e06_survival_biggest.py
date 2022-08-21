numbers = list(map(int, input().split(' ')))
n = int(input())

for i in range(n):
    numbers.remove(min(numbers))

new_string = ", ".join(map(str, numbers))
print(new_string)