planned_gifts = input().split(' ')

cmd = input().split(' ')
while cmd[0] != 'No' and cmd[1] != 'Money':
    if cmd[0] == "OutOfStock":
        gift = cmd[1]
        planned_gifts = list(map(lambda x: x.replace(gift, "None"), planned_gifts))

    if cmd[0] == "Required" and 0 < int(cmd[2]) <= int(len(planned_gifts)):
        planned_gifts[int(cmd[2])] = (cmd[1])

    if cmd[0] == "JustInCase":
        planned_gifts[-1] = cmd[1]

    cmd = input().split(' ')

while "None" in planned_gifts:
    planned_gifts.remove("None")

print(' '.join(planned_gifts))