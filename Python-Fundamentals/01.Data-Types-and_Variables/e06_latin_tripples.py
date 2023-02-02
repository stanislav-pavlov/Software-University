num_letters = int(input())

for i in range(0, num_letters):
    for k in range(0, num_letters):
        for j in range(0, num_letters):
            print(f"{chr(97+i)}{chr(97+k)}{chr(97+j)}")
