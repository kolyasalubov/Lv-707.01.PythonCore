def maximizing_or_minimizing(a, b):
    """ 
    This function defines either
    maximum or minimum of two numbers
    """
    if a > b:
        print(f"number {a} is bigger than  {b}")
    elif a < b:
        print(f"number {b} is bigger than  {a}")   
    else:
        print(f"number {a} equals to  {b}")   

maximizing_or_minimizing(43, 43)