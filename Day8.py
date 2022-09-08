# -------------------------------------More about strings------------------------------------------
# The join string is used to conactenate the different values together.
# Also the join has a syntax => '<string>'.join(list\tuple)
"""
colours = ';'.join(['Ti','Ai','Ci']) #here the semi colon is the string 
                                     #that is used to concatenate the list
print(colours)

a_new_text = ''.join(('Hello ','There!'))
print(a_new_text)
"""

# The other useful function is partition
# This partition unpacks using a seperator and then gives the output as a tuple
# The syntax is =>  'String'.partition('<String that should be used to partition before and after>')
"""
x = 'SatyarajCh'.partition('raj') #here raj is used to partition the string
print(x)

a,sep_str,b = 'This is a :this is b'.partition(':')
print(a)
print(b)


# F-Strings: This will make the formmating easier
# before a string we place an f and pass the value directly
# refer to internet for more details

value = 4 * 4
f'The value is {value}'
"""

#------------------------------------------Ranges----------------------------------------------
# Ranges have 3 syntaxes => 1. range(stop value)
#                           2. range(start value, stop value)
#                           3. range(start value, stop value, step up/ skip the number of values)
"""
x = [20,33,1,43,42,1354]
for i in range(len(x)):
    print(x[i])
#The above code works but it is not good to use instead we will use the enumerate function
"""
x = [20,33,1,43,42,1354]
#for t in enumerate(x):
#    print(t)

for indexxx, valueee  in enumerate(x):
    print(f'Index = {indexxx}, Value = {valueee}')
