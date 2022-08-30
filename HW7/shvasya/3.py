def count(hello):
    """
    This function calculates the number of
    characters in a given string
    """
    list = [i for i in hello]
    dict = {}
    for item in list:
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1
    return dict        
    print("Numbers of characters are as following :",dict)        

print("Numbers of characters are as following :", count("afafafaf"))