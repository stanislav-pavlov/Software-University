def num_classifier(nums):
    positive_nums = [str(num) for num in nums if num >= 0]
    negative_nums = [str(num) for num in nums if num < 0]
    even_nums = [str(num) for num in nums if num % 2 == 0]
    odd_nums = [str(num) for num in nums if num % 2 != 0]

    print(f"Positive: {', '.join(positive_nums)}")
    print(f"Negative: {', '.join(negative_nums)}")
    print(f"Even: {', '.join(even_nums)}")
    print(f"Odd: {', '.join(odd_nums)}")


data = list(map(int, input().split(", ")))
num_classifier(data)