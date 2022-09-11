def heart_delivery(hearts_to_deliver):
    cmd = input()
    visited_house_index = 0

    while cmd != "Love!":
        cmd_elements = cmd.split(" ")
        length = int(cmd_elements[1])

        visited_house_index = visited_house_index + length
        if visited_house_index not in range(len(hearts_to_deliver)):
            visited_house_index = 0

        if hearts_to_deliver[visited_house_index] == 0:
            print(f"Place {visited_house_index} already had Valentine's day.")
        else:
            hearts_to_deliver[visited_house_index] -= 2
            if hearts_to_deliver[visited_house_index] == 0:
                print(f"Place {visited_house_index} has Valentine's day.")
        cmd = input()

    print(f"Cupid's last position was {visited_house_index}.")

    if all(element == 0 for element in hearts_to_deliver):
        print("Mission was successful.")
    else:
        print(f"Cupid has failed {sum(x != 0 for x in hearts_to_deliver)} places.")


hearts_remaining_each_house = list(map(int, input().split('@')))
heart_delivery(hearts_remaining_each_house)