def check_age():
    try:
        input_age = int(input("Enter your age: "))
        if input_age < 0:
            raise ValueError("You entered incorrect data.")
    except ValueError:
        return "You entered incorrect data."
    else:
        return f"Age {input_age} is even" if input_age % 2 == 0 else f"Age {input_age} is odd"


print(check_age())
