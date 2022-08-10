numLetters = int(input())

for i in range(0, numLetters):
    for k in range(0, numLetters):
        for j in range(0, numLetters):
            print(f"{chr(97+i)}{chr(97+k)}{chr(97+j)}")