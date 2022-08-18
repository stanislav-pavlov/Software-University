red_cards = input().split(' ')
team_A = 11
team_B = 11
penalised_list = []
termination_condition = False

for card in red_cards:
    if card not in penalised_list:
        penalised_list.append(card)
        if 'A' in card:
            team_A -= 1
        elif 'B' in card:
            team_B -= 1

    if team_A < 7 or team_B < 7:
        termination_condition = True
        break

print(f"Team A - {team_A}; Team B - {team_B}")

if termination_condition:
    print("Game was terminated")