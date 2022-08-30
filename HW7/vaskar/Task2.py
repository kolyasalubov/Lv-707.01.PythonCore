def rectangle_area():
    """
    rectangle_area takes width and height of a rectangle to calculate area
    """
    a = float(input('enter height: '))
    b = float(input('enter width: '))
    area = a*b
    return area, 'square units'

def right_triangle_area():
    """
    right_triangle_area to calculate area of a right triangle
    takes two arguments as cathetuses(legs)
    """
    a =float(input('enter 1st cathetus(leg): '))
    b=float(input('enter 2nd cathetus(leg): '))
    area = 0.5*a*b
    return area, 'square units'

def circle_area():
    """
    circle_area calculates area of a circle
    takes 1 positinal argument r - radius(R)
    pi is given at 3.1415 accuracy
    """
    r = float(input('please enter raduis of your circle: '))
    pi = 3.1415
    area = pi*r**2
    return area, 'square units'

user_choice = int(input('Choose your figure. Press 1 for rectangle, 2 for triange, 3 for circle'))
if user_choice ==1:
    print(rectangle_area())
elif user_choice == 2:
    print(right_triangle_area())
elif user_choice ==3:
    print(circle_area())
else:
    print('Choose your figure. Press 1 for rectangle, 2 for triange, 3 for circle')

