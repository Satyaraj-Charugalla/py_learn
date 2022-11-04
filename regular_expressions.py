import re      # Importing the regular expressions module
"""
fhand = open('mbox-short.txt')
count = 0
#To understand the search function in the re module
for lin in fhand:
    lin = lin.rstrip() #To remove the spaceing or the \n at the end of the line
    if re.search('From:',lin): 
        # The search will return a true or false
        # So the function will search for the word 'From' in the line
        print(lin)
        count = count + 1
print(f'Number of lines are {count}')
"""
"""
# To understand the wildcards used in the search
fhand = open('mbox-short.txt')
count = 0
for lin in fhand:
    lin = lin.rstrip() #To remove the spaceing or the \n at the end of the line
    if re.search('^From:',lin): 
        # Now it will search for the words that startwith From. 
        # Similar to line.startswith('From:')
        print(lin)
        count = count + 1
print(f'Number of lines are {count}')
"""
"""
# To understand how multiple wildcards can be used at a time
fhand = open('mbox-short.txt')
count = 0
for lin in fhand:
    lin = lin.rstrip() #To remove the spaceing or the \n at the end of the line
    if re.search('^F.*:',lin): 
        # The word should start with F(^F) followed by any number of charcter(.*) between F and :
        print(lin)
        count = count + 1
print(f'Number of lines are {count}')
"""

#----------------------------Extracting data using regex---------------------
random_string = '2 plus 2 is 4 not 22'
y = re.findall('[0-9]+',random_string) 
# The [0-9]+ will search for any characters within the range 0 to 9 
# and plus(+) is one more characters. Returns list
z = re.findall('[^0-9]+',random_string)
# The [^0-9]+ will return characters that do not fall within the range 0 to 9.Returns list
print(y)
print(z)