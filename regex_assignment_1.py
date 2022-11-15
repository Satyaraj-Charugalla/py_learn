import re
fhand = open('regex_sum_1657492.txt')
number_store = list()
total_sum = 0
for numbered_lines in fhand:
    number_handler = re.findall('[0-9]+',numbered_lines)
    number_store = number_store+ number_handler

for num in number_store:
    total_sum = total_sum+int(num)
print(total_sum)