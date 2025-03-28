import math


class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def main():
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    shapes = [circle, rectangle]

    print("Shape Areas:")
    for shape in shapes:
        print(f"{shape.__class__.__name__} Area: {shape.area():.2f}")


if __name__ == "__main__":
    main()
