# Task 3

# Method #1
x = 10
y = 20
print("x: {}, y: {}".format(x, y))

x , y = y, x
print("x: {}, y: {}".format(x, y))

# Method #2
x = 15
y = 20
print("x: {}, y: {}".format(x, y))

x += y
y = x - y
x = x - y
print("x: {}, y: {}".format(x, y))