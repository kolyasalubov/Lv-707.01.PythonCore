x = int (input ())
kol = 0
kol_ch = 0
s = 0
pr = 1
maxim = 0
minim = 9
while x > 0 :
    last = x % 10
    kol = kol + 1
    if last % 2 == 0 :
        kol_ch += 1
    s = s + last
    pr = pr * last
    if last > maxim :
        maxim = last
    if last < minim :
        minim = last
    x = x // 10
print ("Всего цифр:", kol)
print ("Всего четних цифр:",kol_ch )
print ("Summ",s)
print ("derivative",pr)
print ("Maxim",maxim)
print ("Minim",minim)