import math


def find_area_circle(radius: int) -> float:
    '''
    :param radius: radius of circle
    :return: area of circle
    '''
    return math.pi * radius ** 2


def find_area_rect(weight: int, height: int) -> float:
    '''
    :param weight, height: weight and height of rect
    :return: area of rect
    '''
    return weight * height


def find_area_triangle(a: int, b: int, c: int) -> float:
    '''
    :param a, b, c: side of triangle
    :return: area of triangle
    '''
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


type_of_operation = input("Enter type of figure for calculate area(1-rectangle, 2-triangle or 3-circle):")
match type_of_operation:
    case 'circle' | '3':
        r = int(input('Enter radius of circle:'))
        print(f"Area of circle = {round(find_area_circle(r), 2)}")
    case 'rectangle' | '1':
        a = (int(num) for num in input("Enter side a and b of rectangle use space between:").split())
        print(f"Area of rectangle = {round(find_area_rect(*a), 2)}")
    case 'triangle' | '2':
        a = (int(num) for num in input("Enter side a, b, c of triangle use space between:").split())
        print(f"Area of triangle = {round(find_area_triangle(*a), 2)}")
    case _:
        print('Not correct choice! Program error!')
