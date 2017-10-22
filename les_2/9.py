# 9. Write a script to replace last value of tuples in a list.
# 		Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# 		Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

x_tuple = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print(list(filter(None,x_tuple)))
