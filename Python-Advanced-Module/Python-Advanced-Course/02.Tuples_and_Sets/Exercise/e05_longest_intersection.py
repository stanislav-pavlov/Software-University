N = int(input())
longest_intersection = ''


for _ in range(N):
    first_range, second_range = input().split('-')
    first_set = set()
    second_set = set()

#    first_range = first_range.split(',')
#    r1_start, r1_end = tuple(first_range)
    # softuni solved it:
    r1_start, r1_end = tuple(map(int, first_range.split(',')))
    for x in range(r1_start, r1_end+1):
        first_set.add(x)
    # my way:
    second_range = second_range.split(',')
    r2_start, r2_end = tuple(second_range)
    for y in range(int(r2_start), int(r2_end)+1):
        second_set.add(y)

    if len(first_set & second_set) > len(longest_intersection):
        longest_intersection = first_set & second_set

print(f"Longest intersection is [{str(longest_intersection).replace(str(longest_intersection)[0],'').replace(str(longest_intersection)[-1],'')}] with length {len(longest_intersection)}")

# my initial way, same output, not recognised by Judge:
# print(f"Longest intersection is [{str(longest_intersection).removeprefix('{').removesuffix('}')}] with length {len(longest_intersection)}")

# softuni solved it:
# print(f"Longest intersection is [{', '.join(map(str, {el for el in longest_intersection}))}] with length {len(longest_intersection)}")