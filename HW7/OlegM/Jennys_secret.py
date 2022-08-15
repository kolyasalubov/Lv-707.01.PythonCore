def greet(name: str):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)


print(greet("Johnny"))
print(greet("Harold"))