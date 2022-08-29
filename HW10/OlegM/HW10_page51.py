class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input(f"Enter side of rectangle {str(i + 1)}: ")) for i in range(self.n)]
        if not self.verifySiges():
            print("Not correct sizes of rectangle. Enter again.")
            self.inputSides()

    def verifySiges(self):
        if self.n == 2:
            return all([self.sides[i] > 0 for i in range(self.n)])

    def dispSides(self):
        print(*[f"Side {i + 1} is {self.sides[i]}" for i in range(self.n)], sep='\n')


class Rectangle(Polygon):
    def __init__(self):
        super(Rectangle, self).__init__(2)


    def findArea(self):
        a, b = self.sides
        area = (a * b)
        return f"The area of the rectangle is {area}"

    def findPerimer(self):
        a, b = self.sides
        perimetr = (a + b) * 2
        return f"The area of the rectangle is {perimetr}"


tr = Rectangle()
tr.inputSides()
tr.dispSides()
print(tr.findArea())
print(tr.findPerimer())
