import math

def get_area_rectangle():
    input_lenght = float(input("Enter the lenght value: "))
    input_widht = float(input("Enter the widht value: "))
    return "Area of a rectangle = {}".format(input_lenght * input_widht)

def get_area_triangle():
    input_side = float(input("Enter the side value: "))
    input_height = float(input("Enter the height value: "))
    return "Area of a triangle = {}".format(0.5 * input_side * input_height)

def get_area_circle():
    input_radius = float(input("Enter the radius value: "))
    return "Area of a circle = {}".format(round(math.pi * math.pow(input_radius, 2), 3))
