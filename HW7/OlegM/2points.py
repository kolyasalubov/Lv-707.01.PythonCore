def distance(x1: int, y1: int, x2: int, y2: int) -> float:
    '''calculate the distance between between two point'''
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)


print(distance(0, 0, 3, 4))
