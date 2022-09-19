data = input().split(" ")
searched_product = input().split(" ")

stock = {}

for i in range(0, len(data), 2):
    product = data[i]
    quantity = int(data[i+1])
    stock[product] = quantity

for sp in searched_product:
    if sp in stock:
        print(f"We have {stock[sp]} of {sp} left")
    else:
        print(f"Sorry, we don't have {sp}")