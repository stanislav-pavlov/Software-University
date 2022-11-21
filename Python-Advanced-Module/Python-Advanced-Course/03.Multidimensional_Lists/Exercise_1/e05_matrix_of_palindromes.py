import string
alphabet = list(string.ascii_lowercase)

rows, columns = tuple(map(int, input().split()))
matrix = []
idx_mid_letter_start = -1

for r in range(rows):
    first_and_last_letter = alphabet[r]
    idx_mid_letter_start += 1
    row = []
    for c in range(columns):
        mid_letter = alphabet[c+idx_mid_letter_start]
        result = first_and_last_letter + mid_letter + first_and_last_letter
        row.append(result)
    print(*row)