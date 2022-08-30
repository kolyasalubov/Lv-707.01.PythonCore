"""
We need a function that counts the number of sheep present in the array (true means present).
Don't forget to check for bad values like null/undefined
"""
sheep = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

def count_sheeps(sheep):
    for item in sheep:
        if item == True:
            result_of_count = sheep.count(item)
        else:
            result = sheep.count(item)
    print(f"Result of amount False or null or undefined are: {result}")
    return result_of_count    

print(f"Result of amount sheeps are: {count_sheeps(sheep)}")
