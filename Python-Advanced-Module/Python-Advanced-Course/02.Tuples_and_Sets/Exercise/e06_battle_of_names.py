N = int(input())
odd_set = set()
even_set = set()


for divisor in range(1, N+1):
    name = input()
    ASCII_sum = 0
    for ch in name:
        ASCII_sum += ord(ch)
    result = ASCII_sum // divisor

    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)

odd_sum = sum(odd_set)
even_sum = sum(even_set)
if odd_sum == even_sum:
    print(f"{str(odd_set | even_set).replace('{', '').replace('}', '')}")
elif odd_sum > even_sum:
    print(f"{str(odd_set - even_set).replace('{', '').replace('}', '')}")
else:
    print(f"{str(odd_set ^ even_set).replace('{', '').replace('}', '')}")