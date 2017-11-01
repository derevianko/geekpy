# 1.1 task
# func seasons
# create func
def seasons():
# input number in month
    month = int(input('Input number of month:\n >_ '))
    m_dict = {
    1: ['winter', 'January'],
    2: ['winter', 'February'],
    3: ['spring', 'March'],
    4: ['spring', 'April'],
    5: ['spring', 'May'],
    6: ['summer', 'June'],
    7: ['summer', 'July'],
    8: ['summer', 'August'],
    9: ['autumn', 'September'],
    10: ['autumn', 'October'],
    11: ['autumn', 'November'],
    12: ['winter', 'December'],
    }
    print(m_dict.get(month))
# run func
seasons()

# 1.2 task
# func seasons
# create func
def seasons(month):
# input number in month

    m_dict = {
    1: ['winter', 'January'],
    2: ['winter', 'February'],
    3: ['spring', 'March'],
    4: ['spring', 'April'],
    5: ['spring', 'May'],
    6: ['summer', 'June'],
    7: ['summer', 'July'],
    8: ['summer', 'August'],
    9: ['autumn', 'September'],
    10: ['autumn', 'October'],
    11: ['autumn', 'November'],
    12: ['winter', 'December'],
    }
    print(m_dict.get(month))

# run func, enter in arguments some number from 1 as 12
seasons(1)



# 7 task
# create func calc
def calc():
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

calc()
