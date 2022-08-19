def count_sheeps(sheep):
    return sum(int(i) for i in sheep if i!=None)
count_sheeps([]) 
#please insert the list of sheeps, 
#where some sheep may be missing from their place (True for present).