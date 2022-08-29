def rectangleArea(length, width):
    return length*width

def circleArea(radius):
    return 3.141592653589793*radius**2

def triangleArea(base, perpend_height):
    return (base*perpend_height)/2

figure = input('Enter the figure which area you want to calculate: ')

#if figure.lower()!='triangle' and figure.lower()!='circle' and figure.lower()!='rectangle':
    #print ('Wrong option:(')

if figure.lower()=='triangle':
    area = triangleArea(base=float(input('Enter the base: ')), perpend_height=float(input('Enter the perpenicular height: ')))
    print (f'Area of the {figure} is ~ {round(area, 2)}')
elif figure.lower()=='circle':
    area = circleArea(radius=float(input('Enter the radius: ')))
    print (f'Area of the {figure} is ~ {round(area, 2)}')
elif figure.lower()=='rectangle':
    area = rectangleArea(length=float(input('Enter the length: ')), height=float(input('Enter the height: ')))
    print (f'Area of the {figure} is ~ {round(area, 2)}')
else:
    print ('Wrong option:(')