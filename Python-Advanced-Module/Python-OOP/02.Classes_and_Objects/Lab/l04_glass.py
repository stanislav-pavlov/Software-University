class Glass:
    capacity = 250
    initial_content = 0

    def __init__(self):
        self.content = self.initial_content

    def calculate_space_left(self):
        return self.capacity - self.content

    def fill(self, ml):
        space_left = self.calculate_space_left()
        if space_left > ml:
            self.content += ml
            return f"Glass filled with {ml} ml"
        return f"Cannot add {ml} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        space_left = self.calculate_space_left()
        return f"{space_left} ml left"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
