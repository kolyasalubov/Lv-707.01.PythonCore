def maxFunc(arg1, arg2):
    '''
Parameters:
int arg1 = first number
int arg2 = second number 

Output: 
int: The largest number of two numbers 
or message about numbers having equal value
    
    '''
    #return (max(arg1, arg2) if arg1!=arg2 else print('The entered numbers are equal'))
    if arg1==arg2:
        print('The entered numbers are equal')
    else:
        print(f'Max: {arg1}' if arg1>arg2 else f'Max: {arg2}') 

print(maxFunc.__doc__)
maxFunc(int(input('First number: ')), int(input('Second number: ')))