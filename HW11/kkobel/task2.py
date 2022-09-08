from datetime import date


def getting_day(days: int):
    '''
    Write a program that analyzes the entered number and, depending on the number, gives
    the day of the week that corresponds to this number (1 is Monday, 2 is Tuesday, etc.). 
    Take into account cases of entering numbers from 8 and more, as well as cases of entering non-
    numerical data.
    '''
    try:
        your_date = (date(2022, 9, int(f"{days}")).ctime()).split(" ")
        your_number_of_day = your_date[3]

        your_day = your_date[0]
        try:
            if isinstance(days, int) and 1 <= days < len(your_date):
               print(f"{your_number_of_day} - {your_day}")
        except:       
            raise TypeError(f"Your type of data {days} is not correct")  
        return your_date                 
    except ValueError:
        return (f"This day of week {days} is not correct")
    except TypeError as e:
        return (f"{e}")

print(getting_day(input('Enter your number: ')))
