import sys
"""
# run from command line using the command python files.py Open_files.txt
f = open(sys.argv[1], mode = 'rt', encoding='utf-8')
for line in f:
    #print(line)
    sys.stdout.write(line) # this will remove or strip the empty white spaces

f.close()
"""

"""
from itertools import count, islice,slice

def seq():
    #Generate Recaman's sequence
    seen = set()
    a =0
    for n in count(1):
        yield(a)
        seen.add(a)
        c =a-n
        if c < 0 or c in seen:
            c = a+n
        a = c

def write_seq(filename,numm):
    f = open(filename, mode = 'wt', encoding = 'utf-8')
    f.writeline(f"{r}\n" for r in islice(seq(),numm+1))
    f.close()
"""

fname = 'mbox-short.txt'
fh = open(fname)
email =[]
for line in fh:
    if line.startswith('From:'):
        piec = line.split()
        email.append(piec[1])
print(email)