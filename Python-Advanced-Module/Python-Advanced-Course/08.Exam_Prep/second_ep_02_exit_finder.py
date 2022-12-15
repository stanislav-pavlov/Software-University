names = input().split(', ')

if names[0] == "Tom":
    player_one = "Tom"
    player_two = "Jerry"
else:
    player_one = "Jerry"
    player_two = "Tom"

players_info = [[player_one, "awake"], [player_two, "awake"]]

size = 6
board = []
for r in range(size):
    line = input().split()
    board.append(line)

coordinates = input()
while True:
    row = int(coordinates[1])
    col = int(coordinates[4])
    player_new_pos = board[row][col]

    if players_info[0][1] == "sleeping":
        players_info[0][1] = "awake"
        players_info.append(players_info.pop(0))
        coordinates = input()
        continue

    if player_new_pos == "E":
        print(f"{players_info[0][0]} found the Exit and wins the game!")
        exit()
    elif player_new_pos == "T":
        print(f"{players_info[0][0]} is out of the game! The winner is {players_info[1][0]}.")
        exit()
    elif player_new_pos == "W":
        print(f"{players_info[0][0]} hits a wall and needs to rest.")
        players_info[0][1] = "sleeping"

    players_info.append(players_info.pop(0))
    coordinates = input()