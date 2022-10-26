number_of_heroes = int(input())
heroes = dict()

for i in range(number_of_heroes):
    current_hero = input().split(" ")
    hero_name = current_hero[0]
    hp = int(current_hero[1])
    mp = int(current_hero[2])

    current_hero_dict = dict()
    current_hero_dict['HP'] = hp
    current_hero_dict['MP'] = mp
    heroes[hero_name] = current_hero_dict

event = input()
while event != "End":
    event = event.split(" - ")
    action = event[0]
    current_hero = event[1]

    if action == "TakeDamage":
        damage = int(event[2])
        attacker = event[3]
        if heroes[current_hero]['HP'] - damage > 0:
            heroes[current_hero]['HP'] -= damage
            print(f"{current_hero} was hit for {damage} HP by {attacker} and now has {heroes[current_hero]['HP']} HP left!")
        else:
            heroes.pop(current_hero)
            print(f"{current_hero} has been killed by {attacker}!")

    elif action == "CastSpell":
        required_mp = int(event[2])
        spell = event[3]
        if heroes[current_hero]['MP'] - required_mp >= 0:
            heroes[current_hero]['MP'] -= required_mp
            print(f"{current_hero} has successfully cast {spell} and now has {heroes[current_hero]['MP']} MP!")
        else:
            print(f"{current_hero} does not have enough MP to cast {spell}!")

    elif action == "Heal":
        healed_amount = int(event[2])
        if heroes[current_hero]['HP'] + healed_amount > 100:
            healed_amount = 100 - heroes[current_hero]['HP']
            heroes[current_hero]['HP'] = 100
        else:
            heroes[current_hero]['HP'] += healed_amount
        print(f"{current_hero} healed for {healed_amount} HP!")

    elif action == "Recharge":
        recharged_mp = int(event[2])
        if heroes[current_hero]['MP'] + recharged_mp > 200:
            recharged_mp = 200 - heroes[current_hero]['MP']
            heroes[current_hero]['MP'] = 200
        else:
            heroes[current_hero]['MP'] += recharged_mp
        print(f"{current_hero} recharged for {recharged_mp} MP!")

    event = input()

for hero in heroes:
    print(f"{hero}")
    print(f"  HP: {heroes[hero]['HP']}")
    print(f"  MP: {heroes[hero]['MP']}")