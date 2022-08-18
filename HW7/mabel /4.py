x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x1: "))
y2 = float(input("Enter y1: "))
def distance(x1, y1, x2, y2):
    return (((x2-x1)**2 + (y2-y1)**2) ** 0.5)
print (distance(x1, y1, x2, y2))