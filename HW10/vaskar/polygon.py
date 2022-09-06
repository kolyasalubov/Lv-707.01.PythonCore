class Polygon():
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for  i in range(no_of_sides)]
    def inputSides(self):
        self.sides = [float(input(f"Enter side {str(i+1)}: ")) for i in range(self.n)]
    
class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 4)
    def find_area(self):
        a,b,c,d = self.sides
        t = list(set(self.sides))
        s = t[0]*t[1]
        return "this is the area", t, s
my_rectangle = Rectangle()
my_rectangle.inputSides()
print(my_rectangle.find_area())
