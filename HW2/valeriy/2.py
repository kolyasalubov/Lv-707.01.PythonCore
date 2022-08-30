num_int = 123
num_flo = 1.23
num_new = num_int + num_flo

print("datatype of num_int:", type(num_int))
print("datatype of num_flo:", type(num_flo))
print("Value of num_new:", num_new)
print("datatype of num_new:", type(num_new))



keyword_order = "{j}, {l} and {k}".format (j="David", k="Olga", l="Misha")
print(keyword_order)

position_order = "{2}, {0} and {1}".format("Oleg", "Anna", "Bogdan")
print(position_order) 