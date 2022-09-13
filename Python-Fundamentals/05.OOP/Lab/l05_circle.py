class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

#   C = 2 x pi x radius
    def calculate_circumference(self):
        return self.diameter * Circle.__pi

#   A = pi * radius ^ 2
    def calculate_area(self):
        return Circle.__pi * (self.radius ** 2)

#   (angle/360º) ×  pi * r^2
    def calculate_area_of_sector(self, angle):
        self.angle = angle
        return (angle / 360) * Circle.__pi * (self.radius ** 2)


diam = int(input())
new_circle = Circle(diam)

angle = int(input())

print(f"{new_circle.calculate_circumference():.2f}")
print(f"{new_circle.calculate_area():.2f}")
print(f"{new_circle.calculate_area_of_sector(angle):.2f}")
