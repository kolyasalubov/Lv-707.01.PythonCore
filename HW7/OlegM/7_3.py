def calculate_symbol(str_in: str) -> dict:
    '''
    Count of symbols in string
    :param str_in: enter string
    :return: dict with count of symbols
    '''
    d = {}
    d = {str(symbol): str_in.count(symbol) for symbol in str_in if symbol not in d}
    return d


str_ = input("Enter string:")
print(f"Result of working: {calculate_symbol(str_)}")