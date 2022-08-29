def distance(x1, y1, x2, y2):
    distance = ((x1-x2)**2+(y1-y2)**2)**(1/2)
    return round(distance,2)


print(distance(1,2,3,4))