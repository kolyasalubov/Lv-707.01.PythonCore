number = 91128999334474
print(len(str(number)))
sep = list(str(number))
print(sep)
product = 1
for a in sep:
    product *=int(a)
print(product)
revers = str(number)[::-1]
print('origin_number: ', number)
print('this is the reverse of the number: ', int(revers))
sorted = []
for a in sep:
    sorted.append(int(a))
print(sorted)
sorted.sort()
print(sorted)