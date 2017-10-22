# 8. Write a script to replace last value of tuples in a list.
# 		Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# 		Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

tup_1 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
a = (10, 20, 100)
b = (40, 50, 100)
c = (70, 80, 100)
tup_1[0] = a
tup_1[1] = b
tup_1[2] = c
print(tup_1)
