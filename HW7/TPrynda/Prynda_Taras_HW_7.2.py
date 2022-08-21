def square():
    """
       This is the function for calculating the square 
       of the Triangle, Rectangle and Circle
    """
    choise=int(input("Choose between the folowing options:\n\
                     1) Type \"1\" to calculate the square of the Triangle\n\
                     2) Type \"2\" to calculate the square of the Rectangle\n\
                     3) Type \"3\" to calculate the square of the Circle\n\
                     Your choise:"))
    if 1<choise>3:
        print("WRONG CHOISE!")
    else:
        match (choise):
            case 1:
                a=float(input("Enter the \"base\" of your Triagnle"))
                b=float(input("Enter the \"heigh\" of your Triagnle"))
                my_square=1/2*a*b
                print(f"Square of your Triangle is:{my_square}")
            case 2:
                a=float(input("Enter the \"width\" of your Rectangle"))
                b=float(input("Enter the \"heigh\" of your Rectangle"))
                my_square=a*b
                print(f"Square of your Rectangle is:{my_square}")
            case 3:
                a=float(input("Enter the \"radius\" of your Circle"))
                
                my_square=3.14*a*a
                print(f"Square of your Circle is:{my_square}")
    return square


square() 
     
