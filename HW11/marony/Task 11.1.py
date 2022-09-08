def age_user(age):
    try: 
        if age<=0:
            raise ValueError('It should be a positive number:)')
        if age%2==0:
            print ("Your age is even")
        if age%2!=0:
            print ("Your age is odd")
    except ValueError as e:
        print (e)
age_user(int(input('Enter your age: ')))