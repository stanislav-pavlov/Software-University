def calculator(operator, a, b):
    if operator == "multiply":
        return a * b
    elif operator == "divide":
        return int(a / b)
    elif operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b


calc_operator = input()
calc_a = int(input())
calc_b = int(input())


print(calculator(calc_operator, calc_a, calc_b))