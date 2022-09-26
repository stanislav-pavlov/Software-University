countries = input().split(', ')
capitals = input().split(', ')
capitals_dictionary = dict(zip(countries, capitals))

#for key, value in capitals_dictionary.items():
#    print(f"{key} -> {value}")

[print(f"{key} -> {value}") for key, value in capitals_dictionary.items()]