data = input()
phonebook = {}

while '-'in data:
    name_nr = data.split('-')
    name = name_nr[0]
    phone_number = name_nr[1]

    phonebook[name] = phone_number

    data = input()

searched_persons_count = int(data)

for i in range(searched_persons_count):
    searched_name = input()

    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")