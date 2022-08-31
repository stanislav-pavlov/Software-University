def palindrome_func(nums):
    for s in nums:
        if s == s[::-1]:
            print("True")
        else:
            print("False")


initial_list = input().split(", ")
palindrome_func(initial_list)