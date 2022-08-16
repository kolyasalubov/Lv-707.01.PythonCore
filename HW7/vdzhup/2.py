def get_area_rectangle(lenght, widht):
    area_rectangle = lenght * widht
    print(f"Area of a rectangle = {area_rectangle}")

def get_area_triangle(side, height):
    area_triangle = 0.5 * side * height
    print(f"Area of a triangle = {area_triangle}")

def get_area_circle(radius):
    PI = 3.14
    area_circle = PI * radius ** 2
    print(f"Area of a circle = {area_circle}")

def return_function(user_func):
    if user_geometric_figure == "rectangle" or user_geometric_figure == "Rectangle":
        return get_area_rectangle(int(input("Enter the lenght value: ")), int(input("Enter the widht value: ")))
    elif user_geometric_figure == "triangle" or user_geometric_figure == "Triangle":
        return get_area_triangle(int(input("Enter the side value: ")), int(input("Enter the height value: ")))
    elif user_geometric_figure == "circle" or user_geometric_figure == "Circle":
        return get_area_circle(int(input("Enter the radius value: ")))


user_geometric_figure = input("Enter the name of the geometric figure to calculate the area: ")
result = return_function(user_geometric_figure)
