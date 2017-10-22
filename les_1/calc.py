opr = str(input('''Select math operation:
+ for addition
- for subtraction
* for multiplication
/ for division
>_ '''))

num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))

if opr == '+':
    print('{} + {} ='.format(num_1, num_2))
    print(num_1 + num_2)
elif opr == '-':
    print('{} - {} ='.format(num_1, num_2))
    print(num_1 - num_2)
elif opr == '*':
    print('{} * {} ='.format(num_1, num_2))
    print(num_1 * num_2)
elif opr == '/':
    print('{} / {} ='.format(num_1, num_2))
    print(num_1 / num_2)
else:
    print('No selected, run calc againe')
