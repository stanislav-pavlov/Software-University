red_cards_list = input().split(' ')
team_A = list(range(1, 11+1, 1))
team_B = list(range(1, 11+1, 1))
removed_players = []
terminate_condition = False

for card in red_cards_list:
    card_info = card.split('-')
    penalised_team = card_info[0]
    penalised_player = card_info[1]
    pen_player_int = int(penalised_player)

    if card in removed_players:
        continue

    if penalised_team == 'A':
        team_A.remove(pen_player_int)
    elif penalised_team == 'B':
        team_B.remove(pen_player_int)

    removed_players.append(card)

    if len(team_A) < 7 or len(team_B) < 7:
        terminate_condition = True
        break

print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
if terminate_condition:
    print("Game was terminated")