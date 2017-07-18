"""
python check_square.py ((((((2, 3)))
input: ((((((2, 3)))
output: ((((((2, 3))))))
"""

import sys
print(f'input : {sys.argv[1]}')

number_of_open_brackets = 0
number_of_close_brackets = 0
for i in range(len(sys.argv[1])):
    if sys.argv[1][i] == '(':
        number_of_open_brackets += 1
    elif sys.argv[1][i] == ')':
        number_of_close_brackets += 1

difference = number_of_open_brackets - number_of_close_brackets
result = sys.argv[1] + difference * ')'

print(f'output : {result}')