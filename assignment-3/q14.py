class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14159 * self.radius

circle = Circle(7)
print("Area of circle:", circle.area())
print("Perimeter of circle:", circle.perimeter())
