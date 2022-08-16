def numMAX(num1: int , num2: int):
    if num2 > num1:
        return 'largest number: ' , num2 
    elif num2 < num1:
        return 'largest number: ' , num1 
    elif num1 == num2:
        print("the numbers are equal")


print(numMAX(int(input('Enter number1: ')) , int(input('Enter number2: '))))

