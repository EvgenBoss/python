x = float(input("Введите вещественное число\n"))
str_x = str(x)
str_x = str_x.replace('.', '')
str_x = str_x.replace('-', '')
lst_str = list(str_x)
lst_num = map(int, lst_str)
s = sum(lst_num)
print(s)