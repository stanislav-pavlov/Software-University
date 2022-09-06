# nums_list = list(map(int, input().split(", ")))
#
# filtered_evens = map(filter(lambda x: x % 2 == 0, nums_list))
#
# print(list(filtered_evens))

nums_list = list(map(int, input().split(", ")))

even_indecies = list()

for i in range(len(nums_list)):
    if nums_list[i] % 2 == 0:
        even_indecies.append(i)

print(even_indecies)