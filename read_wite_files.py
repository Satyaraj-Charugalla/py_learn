"""
fhand = open('Open_files.txt','r') 
# This r will open the file in a read mode
print(fhand.read())
"""

"""
fhand = open('Open_files.txt','a')
# This will open the file in write mode, this will allow the user to append data
fhand.write('\nLine added on 27th Oct 2022')
fhand.close()
# When a file is opened in write or edit mode then the file should be closed
# before going further
fhand = open('Open_files.txt','r') 
print(fhand.read())
"""

fhand = open('Open_file.txt','w')
fhand.write("Shoot :| The file's overwritten.....")
fhand.close()
# The w will overwrite the content in the file so a user should be cautious when using this
fhand = open('Open_file.txt','r')
print(fhand.read())