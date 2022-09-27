n = int(input())
parking_dict = {}
for i in range(n):
    line = input().split(' ')
    command = line[0]
    user = line[1]

    if command == 'register':
        licence_plate = line[2]
        if user in parking_dict.keys():
            print(f"ERROR: already registered with plate number {parking_dict[user]}")
        else:
            parking_dict[user] = licence_plate
            print(f"{user} registered {parking_dict[user]} successfully")

    elif command == 'unregister':
        if user not in parking_dict.keys():
            print(f"ERROR: user {user} not found")
        else:
            parking_dict.pop(f"{user}")
            print(f"{user} unregistered successfully")

for key, value in parking_dict.items():
    print(f"{key} => {value}")