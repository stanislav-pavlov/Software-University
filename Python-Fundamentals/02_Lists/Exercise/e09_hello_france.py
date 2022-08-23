ticket = 150
clothes_max = 50
shoes_max = 35
accessories_max = 20

full_list = input().split("|")
budget = int(input())
copy_initial_budget = budget
selling_prices = []
purchase_prices = []
eligible_to_purchase = False

for pairs in full_list:
    single_pair = pairs.split("->")
    item_type = single_pair[0]
    item_price = float(single_pair[1])
    eligible_to_purchase = False
    if budget >= item_price:
        if item_type == "Clothes" and item_price <= clothes_max:
            eligible_to_purchase = True
        elif item_type == "Shoes" and item_price <= shoes_max:
            eligible_to_purchase = True
        elif item_type == "Accessories" and item_price <= accessories_max:
            eligible_to_purchase = True

        if eligible_to_purchase:
            budget -= item_price
            purchase_prices.append(item_price)
            selling_prices.append(item_price * 1.4)

net_profit = sum(selling_prices) - sum(purchase_prices)


if sum(selling_prices) + budget >= ticket:
    for num in selling_prices:
        print(f"{float(num):.2f}", end=" ")
    print("")
    print(f"Profit: {net_profit:.2f}")
    print("Hello, France!")

else:
    for num in selling_prices:
        print(f"{float(num):.2f}", end=" ")
    print("")
    print(f"Profit: {net_profit:.2f}")
    print("Not enough money.")