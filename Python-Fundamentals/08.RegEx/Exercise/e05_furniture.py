import re

line = input()
pattern = r">>(?P<item>\w+)<<(?P<price>\d+(\.(\d+))?)!(?P<quantity>\d+)"
total_expenditure = 0
print("Bought furniture:")

while line != "Purchase":
    purchase_data = re.finditer(pattern, line)
    for single_purchase in purchase_data:
        item = single_purchase.group("item")
        price = float(single_purchase.group("price"))
        quantity = int(single_purchase.group("quantity"))

        total_expenditure += price * quantity
        print(item)

    line = input()

print(f"Total money spend: {total_expenditure:.2f}")