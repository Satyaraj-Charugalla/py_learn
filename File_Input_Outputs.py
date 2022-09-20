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
f = open('Open_files.txt', mode = 'rt', encoding = 'utf-8')
print(f.readline())
print(f.readline())
f.seek(0)
print(f.readlines())