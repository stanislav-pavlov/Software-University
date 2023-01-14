from Various_Projects.song_album_band_project import Animal
from Various_Projects.song_album_band_project import Worker
from Various_Projects.song_album_band_project import Lion
from Various_Projects.song_album_band_project import Tiger
from Various_Projects.song_album_band_project import Cheetah
from Various_Projects.song_album_band_project import Keeper
from Various_Projects.song_album_band_project import Vet
from Various_Projects.song_album_band_project import Caretaker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for empl in self.workers:
            if empl.name == worker_name:
                self.workers.remove(empl)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_wage_expenses = sum(empl.salary for empl in self.workers)

        if self.__budget < total_wage_expenses:
            return f"You have no budget to pay your workers. They are unhappy"

        self.__budget -= total_wage_expenses
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_care_expenses = sum(wildcat.money_for_care for wildcat in self.animals)
        if self.__budget < total_care_expenses:
            return f"You have no budget to tend the animals. They are unhappy."

        self.__budget -= total_care_expenses
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"

        lions = [repr(wc) for wc in self.animals if isinstance(wc, Lion)]
        tigers = [repr(wc) for wc in self.animals if isinstance(wc, Tiger)]
        cheetahs = [repr(wc) for wc in self.animals if isinstance(wc, Cheetah)]

        result += f"----- {len(lions)} Lions:\n" + '\n'.join(lions) + '\n'
        result += f"----- {len(tigers)} Tigers:\n" + '\n'.join(tigers) + '\n'
        result += f"----- {len(cheetahs)} Cheetahs:\n" + '\n'.join(cheetahs)

        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"

        keepers = [repr(empl) for empl in self.workers if isinstance(empl, Keeper)]
        caretakers = [repr(empl) for empl in self.workers if isinstance(empl, Caretaker)]
        vets = [repr(empl) for empl in self.workers if isinstance(empl, Vet)]

        result += f"----- {len(keepers)} Keepers:\n" + '\n'.join(keepers) + '\n'
        result += f"----- {len(caretakers)} Caretakers:\n" + '\n'.join(caretakers) + '\n'
        result += f"----- {len(vets)} Vets:\n" + '\n'.join(vets)

        return result