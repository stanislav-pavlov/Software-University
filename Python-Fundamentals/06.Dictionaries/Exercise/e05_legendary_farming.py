def print_func(essential_materials_dict, junk_materials_dict, legendary_item_name):
    print(f"{legendary_item_name} obtained!")
    [print(f"{key}: {value}") for key, value in essential_materials_dict.items()]
    [print(f"{key}: {value}") for key, value in junk_materials_dict.items()]


def legendary_farming():
    essential_materials_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
    junk_materials_dict = {}
    legendary_item_obtained = False

    while True:
        line = input().lower().split(" ")

        for quantity, material in zip(line[0::2], line[1::2]):
            quantity = int(quantity)

            if material in essential_materials_dict.keys():
                essential_materials_dict[material] += quantity

                if essential_materials_dict[material] >= 250:
                    legendary_item_obtained = True
                    essential_materials_dict[material] -= 250
                    legendary_item_name = ''

                    if material == 'shards':
                        legendary_item_name = 'Shadowmourne'
                    elif material == 'fragments':
                        legendary_item_name = 'Valanyr'
                    elif material == 'motes':
                        legendary_item_name = 'Dragonwrath'

                    print_func(essential_materials_dict, junk_materials_dict, legendary_item_name)

            elif material not in junk_materials_dict.keys():
                junk_materials_dict[material] = quantity
            else:
                junk_materials_dict[material] += quantity

            if legendary_item_obtained:
                break
        if legendary_item_obtained:
            break


legendary_farming()