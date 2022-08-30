import module1

figure = input("What kind of figure's area you want to calculate? 1 - rectangle, 2 - triangle, 3 - circle")

if figure == '1':
    print(module1.rectangle())
elif figure == '2':
    print(module1.triangle())
elif figure == '3':
    print(module1.circle())
else:
    print("wrong input")    