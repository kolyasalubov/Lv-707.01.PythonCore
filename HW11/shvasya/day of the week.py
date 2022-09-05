number = int(input("enter your number:"))
try:
  if number <= 0:
    raise ValueError("your number can't be negative")
  if number > 7:
    raise Exception("days in the week can't be bigger than 8")  
except ValueError as e:
  print("Your Error is", e)    
except Exception as e:
  print("Your error is that", e)  
else:
  corresp_days = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 
               5: 'Saturday', 6: 'Friday', 7: 'Saturday'}
  for key, val in corresp_days.items():
    if key == number:
      print('A corresponding day to the number entered is {}'.format(val))
finally:
  print("Good job, Vasya")