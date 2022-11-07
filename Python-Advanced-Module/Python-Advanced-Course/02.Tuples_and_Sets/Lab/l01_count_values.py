numbers = tuple(map(float, input().split()))
unique_numbers_dict = {}

for num in numbers:
    occurrences = numbers.count(num)
    if num not in unique_numbers_dict:
        unique_numbers_dict[num] = occurrences

for key, value in unique_numbers_dict.items():
    print(f"{key:.1f} - {value} times")