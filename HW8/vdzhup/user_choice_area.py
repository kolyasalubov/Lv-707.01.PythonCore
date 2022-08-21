import calculate_package.area_calculation

def user_choice():
    input_operation = input("Enter the figure whose area you want to calculate (rectangle, triangle, circle): ")
    match input_operation:
        case "rectangle" | "Rectangle":
            return calculate_package.area_calculation.get_area_rectangle()
        case "triangle" | "Triangle":
            return calculate_package.area_calculation.get_area_triangle()
        case "circle" | "Circle":
            return calculate_package.area_calculation.get_area_circle()
        case _:
            return "Other error"


print(user_choice())
