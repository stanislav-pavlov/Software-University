def nums_comparison(nums):
    positives = []
    negatives = []
    for num in nums:
        if num < 0:
            negatives.append(num)
        elif num > 0:
            positives.append(num)

    print(sum(negatives))
    print(sum(positives))

    if abs(sum(negatives)) > sum(positives):
        print("The negatives are stronger than the positives")
    elif abs(sum(negatives)) < sum(positives):
        print("The positives are stronger than the negatives")


nums = map(int, input().split())
nums_comparison(nums)