#create func
str_int = input('Input some valeus:\n >_ ')
if len(str_int) > 30 and len(str_int) < 50:
    l_str_int = tuple(str_int)
    t_str_int = l_str_int.split("'")
    print(t_str_int)
    print(sum(l_str_int))
    print(len(str_int))
elif len(str_int) < 30:
#print sum all numbers and all words
    print('111')
elif len(str_int) > 50:
#my idia
    print('2222')
else:
    print('3333')
