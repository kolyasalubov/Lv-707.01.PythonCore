
age = int(input("enter your age:"))
def processing_input():
  try: 
    if age < 0:
      raise ValueError(f"your age can't be negative")
  except ValueError as e:
    print("exception occurred",e)
  else:
    if age % 2 == 0:
      print ("Your age {} is even".format(age))
    elif age % 2 == 1:
      print ("Your age {} is odd".format(age))  
  finally:
    print("Good job")

print(processing_input())