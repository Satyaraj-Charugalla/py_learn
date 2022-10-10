#Loops
"""Largest of the list
largest = 0
num_lis = [23,11,211,433,22,3,22]
for i in num_lis:
    if i > largest:
        largest = i
print('The largest in the list', largest)
"""

"""Count of the list
count = 0
for i in [23,11,211,433,22,3,22]:
    count = count +1
    print(count,i)
"""

"""Sum of the umbers in list
total = 0
for i in [23,11,211,433,22,3,22]:
    total = total + i
    print(i,'Sum with next----->',total)
"""

"""Average of the list
count = 0
sum = 0
for i in [23,11,211,433,22,3,22]:
    count = count + 1
    sum = sum + i 
print(f'Average value is {sum/count}')
"""

"""Smallest of the list
smallest = None
num_lis = [23,11,211,433,22,3,22]
for i in num_lis:
    if smallest is None:
        smallest = i
    elif i < smallest:
        smallest = i
print(f'The smallest in the list {int(smallest)}')
"""

"""
# Program that repeatedly prompts a user for integer numbers 
# until the user enters 'done'. Once 'done' is entered, 
# print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and
#  put out an appropriate message and ignore the number
"""
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        newnum = int(num)
    except:
        print('Invalid input')
        continue
    
    if largest is None or largest < newnum:
        largest = newnum
    elif smallest is None or smallest > newnum:
        smallest = newnum

print("Maximum is", largest)
print('Minimum is', smallest)
