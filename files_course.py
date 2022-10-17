#Files in Python

"""
handle = open('Open_files.txt', mode='r')
print(handle)
"""
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
"""

"""
fhand = open('Open_files.txt')
#dataread = fhand.read() #Here the entire data was read by the read() method.
#print(len(dataread))
#print(dataread[:200])
dataread = fhand.read(500) #Here the user is asking to read only 500 bytes of the entire file data
print(dataread)
"""

"""
fhand = open('mbox.txt')
count = 0
for read_through in fhand:
    if read_through.startswith('From:'):
        # The startswith method will be checking if the line or 
        # the data read met the condition given by the user
        count = count + 1

print(f'The total count that starts with From is {count}')
"""

"""
fhand = open('Open_files.txt')
for space_remove in fhand:
    space_remove = space_remove.rstrip()
    if space_remove.startswith('It'):
        print(space_remove)
"""

"""
fhand = input('Enter file name:')
try:
    fhand = open(fhand)
except:
    print('There is no file with the entered name :',fhand)
    quit()

count = 0
for space_remove in fhand:
    space_remove = space_remove.rstrip()
    if space_remove.startswith('It'):
        count = count + 1
print(count)
"""

"""
fhand = open('Open_files.txt')
for space_remove in fhand:
    space_remove = space_remove.rstrip()
    print(space_remove.upper())
"""
