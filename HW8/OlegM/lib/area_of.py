import math


def find_area_circle(radius: int) -> float:
    '''
    :param radius: radius of circle
    :return: area of circle
    '''
    return math.pi * math.pow(radius, 2)


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


