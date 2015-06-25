#!/Python27/python

import math

class square:
    def __init__(self, x):
        self.x = x

    def area(self):
        return self.x * self.x

    def perimeter(self):
        return self.x * 4

    def changeX(self, x):
        self.x = x


class rectangle(square):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return (self.x + self.y) * 2

    def changeY(self, y):
        self.y = y

class circle(square):
    def __init__(self, x):
        self.x = x

    def area(self):
        return math.pi * (self.x) * (self.x)

    def perimeter(self):
        return math.pi * self.x * 2
