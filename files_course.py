#File handling in python
"""
handle = open('Open_files.txt', mode='r')
print(handle)
"""

fhander = open('Open_files.txt',mode = 'r')
# The fhander is the handler which will be the 
# stage or a connection for the files that need to be read or written 
# or whatever the user wants to do
count = 0
for content_read in fhander:
    count = count + 1
    print(content_read)

print(f'Number of lines are {count}')
