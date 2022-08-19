deck = input().split(' ')
shuffles = int(input())
middle_index = int(len(deck) / 2)

first_half = deck[:middle_index]
second_half = deck[middle_index:]

for i in range(shuffles):
    faro = [item for sublist in zip(first_half, second_half) for item in sublist]
    deck = faro
    first_half = deck[:middle_index]
    second_half = deck[middle_index:]

print(deck)