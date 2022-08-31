def area_of_figures(user_choice: str):
    '''
    It is a function -
    that calculates the area of a rectangle,
    triangle and circle
    '''
    def calculate_area_of_rectangle(length: int,width: int):
        area_of_rectangle = length * width
        print(f"Area of rectangle is: {area_of_rectangle}")
    

    def calculate_area_of_triangle(side_a: int, height: int):
        area_of_triangle = int(0.5 * side_a * height) 
        print(f"Area of triangle is: {area_of_triangle}")

    P = 3.14
    def calculate_area_of_circle(radius: int):
        area_of_circle = P*radius*radius
        print(f"Area of circle is: {area_of_circle}")

    if user_choice == "rectangle":
        calculate_area_of_rectangle(int(input("Enter length: ")), int(input("Enter width: ")))
    elif user_choice == "triangle":
        calculate_area_of_triangle(int(input("Enter side_a: ")), int(input("Enter height: ")))
    elif user_choice == "circle":
        calculate_area_of_circle(int(input("Enter radius: ")))
    else:
        print(f"You entered {user_choice}, it is not correct function.Try again")
        user_choice_input = area_of_figures(input("Choice what you have to calculate(rectangle, triangle,circle): "))                 
    
user_choice_input = area_of_figures(input("Choice what Area you have to calculate(rectangle, triangle,circle): "))
