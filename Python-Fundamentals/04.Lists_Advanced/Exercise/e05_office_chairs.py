def office_chairs(number_of_rooms):
    chairs_remaining = 0
    insufficiency = False

    for room in range(1, rooms + 1):
        chairs_and_guests = input().split(" ")
        chairs = chairs_and_guests[0]
        guests = int(chairs_and_guests[1])

        diff = abs(len(chairs) - guests)

        if len(chairs) < guests:
            print(f"{diff} more chairs needed in room {room}")
            insufficiency = True
        elif len(chairs) >= guests:
            chairs_remaining += diff

    if not insufficiency:
        print(f"Game On, {chairs_remaining} free chairs left")


rooms = int(input())
office_chairs(rooms)
