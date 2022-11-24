size = int(input())
wonderland = []

alice_is_here = []
tea_bags = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for r in range(size):
    line = input().split()

    wonderland.append(line)

    if 'A' in line:
        alice_is_here = [r, line.index('A')]
        wonderland[r][alice_is_here[1]] = '*'

while tea_bags < 10:
    move = input()

    row = alice_is_here[0] + directions[move][0]
    col = alice_is_here[1] + directions[move][1]

    if not (0 <= row < size and 0 <= col < size):
        break

    alice_is_here = [row, col]
    current_pos = wonderland[row][col]
    wonderland[row][col] = '*'

    if current_pos == 'R':
        break
    if current_pos.isdigit():
        tea_bags += int(current_pos)

if tea_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

print(*[' '.join(row) for row in wonderland], sep='\n')