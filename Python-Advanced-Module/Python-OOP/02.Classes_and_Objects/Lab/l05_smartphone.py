class Smartphone:
    def __init__(self, memory: int):
        self.memory = memory
        self.memory_used = 0
        self.apps = []
        self.is_on = False

    def power(self):
        self.is_on = not self.is_on

    def install(self, app, app_size):
        if self.calculate_memory_left() < app_size:
            return f"Not enough memory to install {app}"

        else:
            if self.is_on:
                self.memory_used += app_size
                self.apps.append(app)
                return f"Installing {app}"
            else:
                return f"Turn on your phone to install {app}"

    def calculate_memory_left(self):
        return self.memory - self.memory_used

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.calculate_memory_left()}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
