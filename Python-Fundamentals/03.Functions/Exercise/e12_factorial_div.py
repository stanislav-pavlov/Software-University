def factorial_div(num1, num2):
    fact1 = 1
    fact2 = 1

    for i in range(1, num1 + 1):
        fact1 = fact1 * i
    for i in range(1, num2 + 1):
        fact2 = fact2 * i

    print(f"{fact1 / fact2:.2f}")


first_num = int(input())
second_num = int(input())
factorial_div(first_num, second_num)