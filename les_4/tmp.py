import sys, os
input_x = open('quiz_your_name.txt', mode='r')
input_y = open('answears.txt', mode='r')
output_x = open('q.txt', mode='r+')
output_y = open('a.txt', mode='r+')
mas_1 = []
mas_2 = []

for line_x in input_x:
    if '>>' in line_x:
        line_x = line_x.replace('>>', '')
        line_x = line_x.strip()
        print(line_x)
        output_x.writelines(line_x)
        mas_1 = output_x.readlines()
        print(mas_1)

for line_y in input_y:
    line_y = line_y.strip()
    line_y = line_y.replace('=', ': ')
    print(line_y)
    output_y.writelines(line_y)




input_x.close
input_y.close
output_x.close
output_y.close
