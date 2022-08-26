import random

def count_sheeps(sheep):
  count=0  
  for i in sheep:
    if bool(i)==True:
        count+=1
  return count


a=count_sheeps(random.sample(range(0,100),25))

print(a)


















