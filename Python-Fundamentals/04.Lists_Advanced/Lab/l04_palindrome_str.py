initial_list = input().split(" ")
sought_palindrome = input()
all_palindromes_list = []

for word in initial_list:
    rev_list = reversed(word)
    rev_word = "".join(rev_list)
    if rev_word == word:
        all_palindromes_list.append(rev_word)

pal_count = all_palindromes_list.count(sought_palindrome)

print(all_palindromes_list)
print(f"Found palindrome {pal_count} times")

