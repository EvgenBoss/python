x = list(map(int,input('Введите список чисел через пробел ').split()))
z = len(x)
e = 0
k = 0
for l in x:
   k = k + x[e]
   e = e + 2
   if e > z-1:
        break
print(k)
