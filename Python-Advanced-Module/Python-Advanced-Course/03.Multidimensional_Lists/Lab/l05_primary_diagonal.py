size = int(input())
matrix = []
total_sum = 0

for _ in range(size):
    row = [int(x) for x in input().split()]
    matrix.append(row)

for idx in range(size):
    total_sum += matrix[idx][idx]

print(total_sum)


# for i in range(size):
#     nums = list(map(int, input().split()))
#     total_sum += nums[i]
#     print(nums)
# print(total_sum)