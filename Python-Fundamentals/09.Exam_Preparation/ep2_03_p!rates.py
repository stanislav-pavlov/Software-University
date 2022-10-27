line = input()
cities = {}

while line != "Sail":
    data = line.split("||")
    city = data[0]
    population = int(data[1])
    gold = int(data[2])

    if city not in cities:
        cities[city] = [population, gold]

    elif city in cities:
        cities[city][0] += population
        cities[city][1] += gold
    line = input()


command = input()
while command != "End":
    event_data = command.split("=>")
    action = event_data[0]
    target_city = event_data[1]

    if action == "Plunder":
        population_slaughtered = int(event_data[2])
        gold_plundered = int(event_data[3])
        print(f"{target_city} plundered! {gold_plundered} gold stolen, {population_slaughtered} citizens killed.")
        cities[target_city][0] -= population_slaughtered
        cities[target_city][1] -= gold_plundered

        if cities[target_city][0] <= 0 or cities[target_city][1] <= 0:
            print(f"{target_city} has been wiped off the map!")
            cities.pop(target_city)

    elif action == "Prosper":
        gold_added = int(event_data[2])
        if gold_added >= 0:
            cities[target_city][1] += gold_added
            print(f"{gold_added} gold added to the city treasury. {target_city} now has {cities[target_city][1]} gold.")
        else:
            print("Gold added cannot be a negative number!")

    command = input()

if len(cities) > 0:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city in cities:
        print(f"{city} -> Population: {cities[city][0]} citizens, Gold: {cities[city][1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")