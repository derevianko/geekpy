import string
import re

input_filename = 'openerp-server.log'
output_warning  = 'log_warning.txt'
output_error  = 'log_error.txt'
output_critical  = 'log_critical.txt'
output_tmp = 'tmp.txt'

a_input = open(input_filename, mode='r', encoding="utf-8")
a_warning = open(output_warning , mode='r+', encoding="utf-8")
a_error = open(output_error, mode='r+', encoding="utf-8")
a_critical = open(output_critical, mode='r+', encoding="utf-8")

# tmp = open(output_tmp, mode='r+', encoding="utf-8")
my_text = a_input.read()

# NUM STRINGS
# for num, line in enumerate(my_text, 1):
#     output_tmp.write(num + ':' + line.strip() + '\n')

# FIND WARNINGS
search_p = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.+WARNING.+'
# search_p = r'\d+:\W\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
results_w = re.findall(search_p, my_text)
for item in results_w:
    a_warning.write(item + '\n')

# FIND ERRORS
search_p = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.+ERROR.+'
# search_p = r'\d+:\W\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
results_e = re.findall(search_p, my_text)
for item in results_e:
    a_error.write(item + '\n')

# FIND CRITICALS
search_p = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.+CRITICAL.+'
# search_p = r'\d+:\W\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
results_c = re.findall(search_p, my_text)
for item in results_c:
    a_critical.write(item + '\n')

print('WARNINGS: ' + str(len(results_w)))
print('ERRORS: ' + str(len(results_e)))
print('CRITICALS: ' + str(len(results_c)))





a_input.close()
a_warning.close()
a_error.close()
a_critical.close()
# tmp.close()

# TO-DO
# [] - enumerate;
# [] - uniq serch
