def triangle_area(base, height):
    area = 0.5*base*height
    return area

def rectangle_area(base, height):
    area = base*height
    return area

def circle_area(radius):
    PI = 3.14
    area = PI*radius**2
    return area


triangle = triangle_area(2,3)
print(f"result of the triangle function is {triangle}")
rectangle = rectangle_area(43,33)
print(f"result of the rectangle function is {rectangle}")
circle = circle_area(3)
print(f"result of the circle function is {circle}")