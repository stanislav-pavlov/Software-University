handouts_list = list(map(int, input().split(", ")))
beggars = int(input())
count = 0

list_of_beggars = [0] * beggars

for single_handout in handouts_list:
    list_of_beggars[count] += single_handout
    count += 1
    if count >= beggars:
        count = 0
print(list_of_beggars)