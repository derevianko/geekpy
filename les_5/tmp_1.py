input_x = open('quiz_your_name.txt', mode='r')
input_y = open('answears.txt', mode='r')
# output_x = open('q.txt', mode='r+')
# output_y = open('a.txt', mode='r+')

for line_x in input_x:
    if '>>' in line_x:
        line_x = line_x.replace('>>', '')
        line_x = line_x.rsplit()
        # print(line_x)


for line_y in input_y:
    line_y = line_y.replace('=', ': ')
    line_y = line_y.rsplit()
    print(line_y)

input_x.close()
input_y.close()
output_x.close()
output_y.close()
