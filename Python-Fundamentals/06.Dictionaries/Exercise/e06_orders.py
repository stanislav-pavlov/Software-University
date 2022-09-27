def orders_func(orders_dict, data):
    product = data[0]
    price = float(data[1])
    quantity = int(data[2])

    if product not in orders_dict.keys():
        orders_dict[product] = [price, quantity]
    else:
        orders_dict[product] = [price, (quantity + orders_dict[product][1])]

    return orders_dict


def groceries():
    line = input()
    orders_dict = {}

    while line != "buy":
        data = line.split(' ')
        orders_dict = orders_func(orders_dict, data)
        line = input()

    for k in orders_dict:
        total_sum_per_product = orders_dict[k][0] * orders_dict[k][1]
        print(f"{k} -> {total_sum_per_product:.2f}")


groceries()