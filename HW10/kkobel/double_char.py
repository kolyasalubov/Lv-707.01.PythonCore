def double_char(string):
    return "".join(element*2 for element in string)


print(f"Result: {double_char('String')}")
print(f"Result: {double_char('Hello World')}")
print(f"Result: {double_char('12345!')}")
