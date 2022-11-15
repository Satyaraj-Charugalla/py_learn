import re 
"""
fhand = open('mbox-short.txt')
count = 0
z = []
for lines in fhand:
    if re.search('^From:',lines):
        mail_ids = re.findall('\S+@\S+',lines)
        z.append(mail_ids)
        count = count + 1
print(f'Number of emails {count}\n')
print(z)
"""
"""
fhand = open('mbox-short.txt')
count = 0
z = []
for lines in fhand:
    if re.search('^From:',lines):
        mail_ids = re.findall('\S+?@\S+',lines)
        count = count + 1
        z.append(mail_ids)

print(f'Number of emails {count}\n')
print(z)
"""

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@(\S+)', x) #This will extract the data after @ until a n empty space comes in
print(y)