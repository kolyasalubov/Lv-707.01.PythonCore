def calculate_symbol(str_in: str) -> dict:
    d = dict()
    for symbol in str_in:
        d[symbol] = d.get(symbol, 0) + 1
    return d


str_ = input("Enter string:")
print(f"Result of working: {calculate_symbol(str_)}")