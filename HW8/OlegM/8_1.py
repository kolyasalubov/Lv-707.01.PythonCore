import lib.area_of as area

type_of_operation = input("Enter type of figure for calculate area(1-rectangle, 2-triangle or 3-circle):")
match type_of_operation:
    case 'circle' | '3':
        r = int(input('Enter radius of circle:'))
        print(f"Area of circle = {round(area.find_area_circle(r), 2)}")
    case 'rectangle' | '1':
        a = (int(num) for num in input("Enter side a and b of rectangle use space between:").split())
        print(f"Area of rectangle = {round(area.find_area_rect(*a), 2)}")
    case 'triangle' | '2':
        a = (int(num) for num in input("Enter side a, b, c of triangle use space between:").split())
        print(f"Area of triangle = {round(area.find_area_triangle(*a), 2)}")
    case _:
        print('Not correct choice! Program error!')
