def create_force_side(side, user, force_dict):
    condition = [current_side for current_side in force_dict if user in force_dict[current_side]]

    if len(condition) == 0:
        if side not in force_dict.keys():
            force_dict[side] = [user]
        else:
            force_dict[side].append(user)

    return force_dict


def create_force_user(user, side, force_dict):
    for current_side in force_dict.keys():
        if user in force_dict[current_side]:
            if len(force_dict[current_side]) > 1:
                force_dict[current_side].pop(user)
                break
            else:
                del force_dict[current_side]
                break

    if side in force_dict:
        force_dict[side].append(user)
    else:
        force_dict[side] = [user]

    print(f"{user} joins the {side} side!")


def force_book():
    line = input()
    force_dict = {}

    while line != "Lumpawaroo":
        if '|' in line:
            data = line.split(' | ')
            side = data[0]
            user = data[1]
            create_force_side(side, user, force_dict)

        elif '->' in line:
            data = line.split(' -> ')
            user = data[0]
            side = data[1]
            create_force_user(user, side, force_dict)

        line = input()

    for side in force_dict.keys():
        print(f"Side: {side}, Members: {len(force_dict[side])}")
        for user in force_dict[side]:
            print(f"! {user}")


force_book()