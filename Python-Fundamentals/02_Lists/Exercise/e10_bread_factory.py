full_list = input().split("|")
energy = 100
coins = 100
closed_bakery = False

for commands in full_list:
    single_command = commands.split("-")
    event_or_ingr = single_command[0]
    amount = int(single_command[1])

    if event_or_ingr == "rest":
        energy += amount
        if energy > 100:
            energy = 100
            print(f"You gained 0 energy.")
        else:
            print(f"You gained {amount} energy.")

        print(f"Current energy: {energy}.")

    elif event_or_ingr == "order":
        energy -= 30
        if energy >= 0:
            coins += amount
            print(f"You earned {amount} coins.")
        else:
            energy += 50
            print("You had to rest!")

# ingredient to buy
    else:
        if coins >= amount:
            coins -= amount
            print(f"You bought {event_or_ingr}.")
        else:
            closed_bakery = True
            break

if closed_bakery == False:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
else:
    print(f"Closed! Cannot afford {event_or_ingr}.")