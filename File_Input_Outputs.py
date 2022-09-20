"""
f = open('Open_files.txt', mode = 'wt', encoding = 'utf-8')
# here the mode wt means Write text sometime we use wb which means Write binary
# or even at => Append text

f.write('Line 1 is added, \n')
f.write('Line 1 continouation is added')
f.close()
"""

"""
f = open('Open_files.txt', mode = 'rt', encoding = 'utf-8')
#print(f.read()) # This will return the entire text inside the file
print(f.read(12)) # This will return the limited number of characters in the file mentioned
f.close()
"""

"""
f = open('Open_files.txt', mode = 'rt', encoding = 'utf-8')
print(f.readline()) # will print 1st line 
print(f.readline()) # will print 2nd line if exists
f.seek(0) # will start from 0 which is it will start the from the begining
print(f.readlines()) # will read all the line in the file
f.close()
"""

f = open('Open_files.txt', mode = 'at', encoding = 'utf-8')
f.writelines([
    'Line 3 is added;\n'
    'Line 4 is added;'
    'Line 5 is added;\n'
])
f.close()