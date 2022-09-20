data = input()
bakery_stock = {}

while data != "statistics":
    data = data.split(": ")

    product = data[0]
    quantity = int(data[1])

    if product not in bakery_stock.keys():
        bakery_stock[product] = quantity
    else:
        bakery_stock[product] += quantity

    data = input()

print("Products in stock:")
[print(f"- {product}: {bakery_stock[product]}") for product in bakery_stock]

print(f"Total Products: {len(bakery_stock.keys())}")
print(f"Total Quantity: {sum(bakery_stock.values())}")