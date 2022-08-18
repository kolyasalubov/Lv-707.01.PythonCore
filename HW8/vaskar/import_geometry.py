import geometry
user_choice = int(input('Choose your figure. Press 1 for rectangle, 2 for triange, 3 for circle'))
if user_choice ==1:
    print(geometry.rectangle_area())
elif user_choice == 2:
    print(geometry.right_triangle_area())
elif user_choice ==3:
    print(geometry.circle_area())
else:
    print('Choose your figure. Press 1 for rectangle, 2 for triange, 3 for circle')