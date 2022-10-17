def additional_func(partition):
    special_chars_max_num = 0
    special_char = ''
    special_chars_list = ['@', '#', '$', '^']
    for ch in partition:
        if ch != special_char:
            if special_chars_max_num >= 6:
                break
            special_chars_max_num = 1
            special_char = ch
        else:
            special_chars_max_num += 1
    return [special_chars_max_num, special_char]


def ticket_validator(ticket):
    ticket_data = ''
    if len(ticket) != 20:
        ticket_data = 'invalid ticket'
    elif ticket[0] * 20 == ticket and ticket[0] in '@#$^':
        ticket_data = f'ticket "{ticket}" - 10{ticket[0]} Jackpot!'
    else:
        winner_source_no_jackpot = ''
        if additional_func(ticket[0:10]) > additional_func(ticket[10:20]):
            winner_source_no_jackpot = additional_func(ticket[10:20])
        else:
            winner_source_no_jackpot = additional_func(ticket[0:10])
        special_syms_num = winner_source_no_jackpot[0]
        special_sym = winner_source_no_jackpot[1]

        if special_syms_num < 6 or special_sym not in '@#$^':
            ticket_data = f'ticket "{ticket}" - no match'
        else:
            ticket_data = f'ticket "{ticket}" - {special_syms_num}{special_sym}'

    return ticket_data


def winning_ticket(tickets):
    for ticket in tickets:
        print(ticket_validator(ticket))


pack_list = input().replace(' ', '').split(',')
winning_ticket(pack_list)