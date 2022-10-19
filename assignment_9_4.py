"""
fname = input("Enter file name: ")
fh = open(fname)
mails = dict()
for line in fh:
    if line.startswith('From '):
        striping = line.rstrip().split()[1]
        mails[striping] = mails.get(striping, 0) + 1
    sender_name = None
    num_of_times_mailed = None
    for keys,values in mails.items():
        if num_of_times_mailed is None or values > num_of_times_mailed:
            num_of_times_mailed = values
            sender_name = keys
print(sender_name,num_of_times_mailed)

fname = input("Enter file name: ")
fh = open(fname)
mails = dict()
x = list()
for line in fh:
    if line.startswith('From '):
        striping = line.rstrip().split()
        x.append(striping[1])
        mails[word] = mails.get(word, 0) + 1
    sender_name = None
    num_of_times_mailed = None
    for keys, values in mails.items():
        if num_of_times_mailed is None or values > num_of_times_mailed:
            sender_name = keys
            num_of_times_mailed = values
print(sender_name,num_of_times_mailed)
"""

fname = input("Enter file name: ")
fh = open(fname)
mails = dict()
x = list()
for line in fh:
    if line.startswith('From '):
        striping = line.rstrip().split()
        x.append(striping[1])
for word in x:
    mails[word] = mails.get(word, 0) + 1
sender_name = None
num_of_times_mailed = None
for keys, values in mails.items():
    if num_of_times_mailed is None or values > num_of_times_mailed:
        sender_name = keys
        num_of_times_mailed = values
print(sender_name,num_of_times_mailed)