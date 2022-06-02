class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def get_area(self):
        return self.a * self.b

    def __eq__(self, other):
        return (self.a == other.a and self.b == other.b) or \
               (self.a == other.b and self.b == other.a)

class Square(Rectangle):
    def __init__(self, a):
        self.a = a

    def get_area_square(self):
        return self.a**2

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'Dot: {self.x} {self.y}'

class Circle:
    pi = 3.14
    def __init__(self, r):
        self.r = r

    def get_area_circle(self):
        return self.pi * (self.r**2)