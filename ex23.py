a = int(input("Введите число полиндром\n"))
def funk(x):
    str_x = str(x)
    str_x = str_x.replace('-', '')
    lst_str = list(str_x)
    lst_num = list(map(int, lst_str))
    lst_new = []
    s = len(lst_str)
    k = s
    print(lst_num)
    for s in range(s):
        lst_new.append(lst_num[k-1])
        k=k-1
    print(lst_new)
    if lst_num == lst_new:
        print("число является полиндромом")
    else:
        a = int(''.join(map(str, lst_new)))
        b = int(''.join(map(str, lst_num)))
        c = a + b
        funk(c)
funk(a)  