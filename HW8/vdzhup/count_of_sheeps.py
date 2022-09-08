def count_sheeps(sheep):
    
    count = [item for item in sheep if item == True]
    return len(count)


print(count_sheeps([True,  True,  True,  False,
            True,  True,  True,  True ,
            True,  False, True,  False,
            True,  False, False, True ,
            True,  True,  True,  True ,
            False, False, True,  True]))
