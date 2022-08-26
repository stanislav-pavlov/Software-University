def bill(product, quantity):
    if product == "coffee":
        return quantity * 1.5
    elif product == "coke":
        return quantity * 1.4
    elif product == "water":
        return quantity * 1
    elif product == "snacks":
        return quantity * 2


item = input()
n = int(input())
print(f"{bill(item, n):.2f}")


# final_bill = bill(item, price, n)