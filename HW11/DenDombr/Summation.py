def summation(num):
    '''
    Write a program that finds the summation of every number from 1 to num. 
    The number will always be a positive integer greater than 0.
    '''
    return sum(element for element in range(1,num+1))

print(f"Suma of numbers are: {summation(2)}")
print(f"Suma of numbers are: {summation(4)}")
print(f"Suma of numbers are: {summation(10)}")