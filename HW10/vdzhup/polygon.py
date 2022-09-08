class CustomException(Exception):

    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return repr(self.message)

class Polygon:

    def __init__(self, num_of_sides):
        self.n = num_of_sides
        self.sides = [0 for item in range(num_of_sides)]

    def inputSides(self):
        self.sides = [float(input(f"Enter side {str(item + 1)}: "))
                                                for item in range(self.n)]

    def dispSides(self):
        for item in range(self.n):
            print(f"Side {item + 1} is {self.sides[item]}")

class Triangle(Polygon):
    
    def __init__(self):
        super().__init__(3)

    def checkSides(self):
        super().dispSides()
        if (((self.sides[0] + self.sides[1]) < self.sides[2])
            or ((self.sides[0] + self.sides[2]) < self.sides[1])
            or ((self.sides[1] + self.sides[2]) < self.sides[0])):
                raise CustomException("The triangle does't exist: the sum of the two sides must be greater than the third")

    def findArea(self):
        a, b, c = self.sides
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print(f"The area of the triangle is {round(area, 3)}")


class Rectangle(Polygon):

    def __init__(self):
        super().__init__(2)

    def findArea(self):
        a, b = self.sides
        area = a * b
        print(f"The area of the rectangle is {round(area, 3)}")


t = Triangle()
t.inputSides()
t.checkSides()
t.findArea()

r = Rectangle()
r.inputSides()
r.dispSides()
r.findArea()
