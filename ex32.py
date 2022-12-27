x = list(map(int,input('Введите список чисел через пробел ').split()))
k = float(len(x))
z,b =0 , 0
for i in x:
    z = x[b]+ x[-(b+1)]
    b = b+1
    if b > (k+1)/2:
        break
    print(z)
