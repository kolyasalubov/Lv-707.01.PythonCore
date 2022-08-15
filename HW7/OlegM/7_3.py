def calculate_symbol(str_in: str) -> dict:
    '''
    Count of symbols in string
    :param str_in: enter string
    :return: dict with count of symbols
    '''
    d = dict()
    for symbol in str_in:
        d[symbol] = d.get(symbol, 0) + 1
    return d


str_ = input("Enter string:")
print(f"Result of working: {calculate_symbol(str_)}")