from collections import deque

egg_sizes = deque(map(int, input().split(', ')))
paper_sizes = deque(map(int, input().split(', ')))
filled_boxes = 0

while egg_sizes and paper_sizes:
    current_egg = egg_sizes.popleft()

    if current_egg <= 0:
        continue

    if current_egg == 13:
        paper_sizes[0], paper_sizes[-1] = paper_sizes[-1], paper_sizes[0]
        continue

    current_paper_piece = paper_sizes.pop()
    current_total = current_egg + current_paper_piece

    if current_total <= 50:
        filled_boxes += 1

if filled_boxes > 0:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if egg_sizes:
    # print("Eggs left: ", end='')
    # print(*egg_sizes, sep=', ')
    print(f"Eggs left: {', '.join(map(str, egg_sizes))}")
if paper_sizes:
    # print("Pieces of paper left: ", end='')
    # print(*paper_sizes, sep=', ')
    print(f"Pieces of paper left: {', '.join(map(str, paper_sizes))}")