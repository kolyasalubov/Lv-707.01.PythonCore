from cmath import pi, sqrt


print ("1-прямокутник,2-трикутник,3=-коло")
figure = input ("Виберіть фігуру: ")

if figure == '1' :
    print ("Довжина сторін прямокутника:")
    a = float (input ("a = "))
    b = float (input ("b = "))
    print ("Площа: %.2f" % (a * b))
elif figure == '2' :
    print ("Довжина сторін трикутника:")
    a = float (input ("a = "))
    b = float (input ("b = "))
    с = float (input ("с = "))
    p = (a + b + c) / 2
    s = sqrt (p * (p - a) * (p - b) * (p - c))
    print ("Площа: %.2f" % s)
elif figure == '3' :
    r = float (input ("Радіус кола R = "))
    print ("Площа: %.2f" % (pi * r ** 2))
else :
    print ("Помилка введення")