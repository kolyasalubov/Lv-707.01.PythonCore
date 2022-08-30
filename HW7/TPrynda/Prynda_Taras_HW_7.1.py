
def min_max(num1, num2):
    """This function is called to determinate 
    the largest number between the 2 given  
    """
    a = max(num1,num2)
    
    if num1==num2:
        print(f"Entered numbers are equal\n num1 = num2 \n    {num1}={num2}")
    else:
        print(f"Max number is:{a}")
    return(a)


l=min_max(44, 44)
print(l, type(l))






