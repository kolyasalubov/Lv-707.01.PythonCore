a = int(input("enter your first number: "))
b = int(input("enter your second number: "))
def qualifier(*args):
    if a>b:
        return a
    elif a==b:
        return "numbers are equal"
    else:
        return b
print(qualifier(a,b))
