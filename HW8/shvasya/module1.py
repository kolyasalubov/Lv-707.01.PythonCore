import math
from math import pow
from math import pi

def rectangle():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    return (f"result is {a * b}") 

def triangle():
    a = float(input("Enter a: "))
    h = float(input("Enter h: "))
    return (f'result is {0.5 * h * a}') 

def circle():
    r = float(input("Enter r: "))
    return (f'result is {pi*pow(r,2)}') 