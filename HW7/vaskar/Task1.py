a = int(input("enter your first number: "))
b = int(input("enter your second number: "))
def qualifier(c,d):
    """
    qualifier takes 2 numbers as arguments to determine the largest one
    """
    if a>b:
        return "largest number is:", a
    elif a==b:
        return "numbers are equal"
    else:
        return "largest number is:", b
print(type(qualifier(a,b)))
