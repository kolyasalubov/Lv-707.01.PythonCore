def distance(x1, x2, y1, y2):
    number = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    print('Distance is:',round(number, 2))
distance(int(input('x1:')), int(input('x2:')), int(input('y1:')), int(input('y2:')))