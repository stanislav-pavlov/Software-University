fights_lost = int (input())
helmet_price = float (input())
sword_price = float (input())
shield_price = float (input())
armor_price = float (input())

total_cost = 0

for current_fight in range(1, fights_lost+1):
    if current_fight % 2 == 0:
        total_cost += helmet_price

    if current_fight % 3 == 0:
        total_cost += sword_price

    if current_fight % 6 == 0:
        total_cost += shield_price

    if current_fight % 12 == 0:
        total_cost += armor_price

print(f"Gladiator expenses: {total_cost:.2f} aureus")
