# 6. Write a script to check whether a specified value is contained in a group of values.
# 		Test Data :
# 		3 -> [1, 5, 8, 3] : True
# 		-1 -> (1, 5, 8, 3) : False

x_str = input ('Enter 5 numbers aross ","')
x_tuple = x_str.split(',')
x_tuple = tuple(x_tuple)
print (x_tuple)
x_num = input ('Search number:')
if x_num in x_tuple:
    print('True')
else:
    print('False')
