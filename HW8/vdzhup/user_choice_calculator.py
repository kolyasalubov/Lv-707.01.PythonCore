import calculate_package.calculator

def user_choice():
    input_operation = input("Enter the operation you want to use (sum, difference, product, division): ")
    match input_operation:
        case "sum" | "Sum":
            return calculate_package.calculator.number_sum()
        case "difference" | "Difference":
            return calculate_package.calculator.number_difference()
        case "product" | "Product":
            return calculate_package.calculator.number_product()
        case "division" | "Division":
            return calculate_package.calculator.number_division()
        case _:
            return "Other error"


print(user_choice())
