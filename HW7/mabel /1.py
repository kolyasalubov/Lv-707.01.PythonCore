def square_area():
    side = int(input('Enter side: '))
    square_a = side**2
    return 'square_area' , square_a 

def square_triangle():
    side_a = int(input('Enter side_a: '))
    side_b = int(input('Enter side_b: '))
    squara_t = 0.5*side_a*side_b
    return 'square triangle' , squara_t 

def square_circle():
   
    radius = int(input('Enter radius: '))
    p = 3.1415
    square = p*radius**2
    return 'square circle' , square


a  =  int(input('''select the area of what you want to calculate
1. Square
2. Triangle
3. Circle 
: '''))

if a == 1 : 
    print(square_area())
elif a ==2 :
    print(square_triangle())
elif a == 3:
    print(square_circle())
else:
    print('Folse')