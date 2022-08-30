a=int(input("Enter your number\n"))
b=str(a)
c=1
print("Number:", a)

print("Reversed number:",b[::-1])

for i in b:
    c*=int(i)
    print(f"i= {i}")
print("Multiplyed members of the number:", c)
s=sorted(b)
r=""
for i in s:
   r+=i
print("Sorted number:", r) 