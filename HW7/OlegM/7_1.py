def find_max(a: int, b: int) -> int:
    '''
    find maximum of two numbers
    :param a: int
    :param b: int
    :return: int
    '''
    return a if a > b else b


a = (int(num) for num in input("Enter two integer numbers use space between numbers:").split())
print(find_max(*a))

