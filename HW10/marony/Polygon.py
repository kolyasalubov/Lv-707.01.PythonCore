class Polygon:
    """
This is Polygon class.
    """
    def __init__(self, num_of_sides):
        self.n=num_of_sides
        self.sides = [0 for i in range(num_of_sides)]
    def inputSides(self):
        self.sides = [float(input(f'Enter side {str(i+1)}: ')) for i in range(self.n)]
    def dispSides(self):
        for i in range(self.n):
            print(f'Side {i+1} is {self.sides[i]}')

class Triangle(Polygon):
    """
This is Triangle class.
    """
    def __init__(self):
        super().__init__(3)

    def findArea(self):
        a, b, c = self.sides
        if max (a, b, c)<(a+b+c-max(a, b, c)):
            s=(a+b+c)/2
            area = (s*(s-a)*(s-b)*(s-c))**0.5
            print(f'The area of triangle is {area}')
        else:
            print('Invalid sides! A triangle exists \nif the sum of every two sides is greater than a third of the sides')
class Quadrangle(Polygon):
    """
This is Quadrangle class.
    """
    def __init__(self):
        super().__init__(4)

    def findArea(self):
        a, b, c, d = self.sides
        s=(a+b+c+d)/2
        area = ((s-a)*(s-b)*(s-c)*(s-d))**0.5 # Формула Брамагупти
        print(f'The area of quadrangle is {area}')
    
q = Quadrangle()
q.inputSides()
q.dispSides()
q.findArea()