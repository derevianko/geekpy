# 3. Write a script to sum of the first n positive integers.

x_num = int(input('Enter number:'))

if x_num > 0:
    x_num += x_num
    print(x_num)
else:
    print('Script end, try again')
