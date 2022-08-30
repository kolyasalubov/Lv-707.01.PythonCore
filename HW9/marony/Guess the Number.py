from random import randint
number=randint(1,100)
print (number)
print('Hello! In this program you need to guess the hidden number \nfrom 1 to 100 (with greater&lesser hints). Good luck!')
user_input=None
while number!=user_input:
    user_input=int(input('Enter the number: ', ))
    if number>user_input:
        print('Oops! That was close. Your number is lesser than the hidden.\nTry again!')
    elif number<user_input:
        print('Oops! That was close. Your number is greater than the hidden.\nTry again!')
print('Wow! Absolutely right! Congratulations!')