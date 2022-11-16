import re
mail_pattern = '[A-Za-z0-9]+@[A-Za-z]+\.(com|net|in)'
mails = input('Enter mail: ')
if re.search(mail_pattern,mails):
    print('Yes')
else:
    print('No')