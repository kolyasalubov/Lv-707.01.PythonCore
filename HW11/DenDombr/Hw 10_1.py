class Polygon:
    '''
    Create a polygon class and a rectangle class
    that inherits from the polygon class and finds the square
    of rectangle.
    '''
    def __init__(self, no_of_sides) -> None:
        self.n = no_of_sides
        self.sides = [0 for element in range(no_of_sides)]

    def input_sides(self):
        self.sides = [float(input(f"Enter your side {element}: ")) for element in range(1,self.n+1)]

    def dispSides(self):
        for element in range(self.n):
            print(f"Side {element+1} is: {self.sides[element]}")    
           

class Rectangle(Polygon):
    def __init__(self) -> None:
        super().__init__(4)

    def square_of_rectangle(self):
        first_side, second_side, third_side, fourth_side = self.sides
        square_of_rectangle = first_side**2 + second_side**2 + third_side**2 + fourth_side**2
        print(f"Square of Rectangle is: {square_of_rectangle}") 

rectangle1 = Rectangle()
rectangle1.input_sides()
rectangle1.dispSides()
rectangle1.square_of_rectangle()   