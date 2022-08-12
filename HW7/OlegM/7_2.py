def find_area(a: int, b: int = 0, c: int =0, type_of_figure: str = "circle" ) -> float:
    '''
    calculates the area of a rectangle, triangle and circle
    :param a: radius or side a of rectangle or side a of triangle
    :param b: side b of rectangle or side b of triangle
    :param c: side c of triangle
    :param type_of_figure: rectangle, triangle and circle for calculates the area
    :return:  the area of a rectangle, triangle and circle
    '''
    match type_of_figure:
        case 'circle':
            return 3.141592*a**2
        case 'rectangle':
            return a*b
        case 'triangle':
            p = (a+b+c)/2
            return (p*(p-a)*(p-b)*(p-c))**0.5



type_of_operation = input("Enter type of figure for calculate area(rectangle, triangle or circle):")
match type_of_operation:
        case 'circle':
            r = int(input('Enter radius of circle:'))
            print(f"Area of circle = {find_area(r, type_of_figure = 'circle')}")
        case 'rectangle':
            a, b = [int(num) for num in input("Enter side a and b of rectangle:").split()][:2]
            print(f"Area of rectangle = {find_area(a, b, type_of_figure='rectangle')}")
        case 'triangle':
            a, b, c = [int(num) for num in input("Enter side a, b, c of triangle:").split()][:3]
            print(f"Area of triangle = {find_area(a, b, c, 'triangle')}")

