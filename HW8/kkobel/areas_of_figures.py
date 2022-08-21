import math


def rectangle(number1: int,number2: int):
    area_of_rectangle = number1*number2
    return area_of_rectangle

def triangle(side_a: int, height: int):
    area_of_triangle = side_a*height*0.5
    return area_of_triangle

def circle(radius: int):
    area_of_circle = math.pi*radius**2
    change_to_two_decimal = '%.2f' % area_of_circle
    return change_to_two_decimal
