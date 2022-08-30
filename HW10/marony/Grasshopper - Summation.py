def summation(num): 
    print (f'Summation of {num} is {sum(i for i in range (num+1))}')
summation(int(input('Enter the number: ')))