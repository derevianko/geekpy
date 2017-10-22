#1 .Write a script which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
#		Sample data : 1, 5, 7, 23
#		Output :
#		List : [‘1', ' 5', ' 7', ' 23']
#		Tuple : (‘1', ' 5', ' 7', ' 23')

# 1 example
x_str=(input('Input some numbers:'))
print(list(x_str))
print(tuple(x_str))

# 2 example
x_str=(input('Input some numbers:'))
x_list=(list(x_str))
x_tuple=(tuple(x_str))
print(x_list)
print(x_tuple)
