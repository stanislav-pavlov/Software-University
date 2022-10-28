price = input()
pre_tax_total = 0
after_tax_total = 0
tax = 0.2

while price != "special" and price != "regular":
    price = float(price)
    if price < 0:
        print("Invalid price!")
    else:
        pre_tax_total += price

    price = input()

if pre_tax_total == 0:
    print("Invalid order!")
else:
    tax_total = pre_tax_total * tax
    after_tax_total = pre_tax_total * (1 + tax)
    if price == "special":
        after_tax_total = after_tax_total * (1 - 0.1)

    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {pre_tax_total:.2f}$")
    print(f"Taxes: {tax_total:.2f}$")
    print("-----------")
    print(f"Total price: {after_tax_total:.2f}$")