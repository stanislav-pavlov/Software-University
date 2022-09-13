class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "bird":
            self.birds.append(name)
        elif species == "fish":
            self.fishes.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ''
        if species == "mammal":
            result += f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}"
        elif species == "bird":
            result += f"Birds in {self.zoo_name}: {', '.join(self.birds)}"
        elif species == "fish":
            result += f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}"
        result += f"\nTotal animals: {Zoo.__animals}"

        return result


name_of_zoo = input()
zoo = Zoo(name_of_zoo)

animals_count = int(input())
for n in range(animals_count):
    species_name = input().split(" ")
    species = species_name[0]
    name_of_animal = species_name[1]
    zoo.add_animal(species, name_of_animal)

sought_species = input()

print(zoo.get_info(sought_species))