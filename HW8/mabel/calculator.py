import square9


def searsh_square():
    square  =  int(input('''select the area of what you want to calculate
1. Square
2. Triangle
3. Circle 
: '''))
    if square == 1:
        return square9.square_area()
    elif square == 2:
        return square9.square_triangle()
    elif square == 3:
        return square9.square_circle()
    else:
        print("not")

print(searsh_square())