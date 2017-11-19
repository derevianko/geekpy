import re

input_file = open('openerp-server.log', mode='r')
for line in input_file:
    line = re.match(r'WARNING')
