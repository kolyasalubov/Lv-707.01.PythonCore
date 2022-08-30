from math import pi , pow

def square_area():
    side_a = int(input('Enter side: '))
    side_b = int(input('Enter side: '))
    square_a = side_a*side_b
    return 'square_area' , square_a 

def square_triangle():
    side_a = int(input('Enter side_a: '))
    side_b = int(input('Enter side_b: '))
    squara_t = 0.5*side_a*side_b
    return 'square triangle' , squara_t 

def square_circle():
   
    radius = int(input('Enter radius: '))
    square = pi*pow(radius,2)
    return 'square circle' , square