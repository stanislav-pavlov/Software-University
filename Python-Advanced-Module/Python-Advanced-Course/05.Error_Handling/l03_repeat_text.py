try:
    line = input()
    N = int(input())
    print(line * N)

except ValueError:
    print("Variable times must be an integer.")

