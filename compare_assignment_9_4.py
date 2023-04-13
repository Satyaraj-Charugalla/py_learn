iread=input('enter the file : ')
fread=open(iread)
oxford=dict()
for line in fread:
    if line.startswith('From '):
        word=line.rstrip().split()[1]
        oxford[word]=oxford.get(word,0)+1
        print(oxford.items())
    """
    maxkey=None
    maxval=None
    for key,value in oxford.items():
        if maxval is None or  value > maxval:
            maxval=value
            maxkey=key
print (maxkey,maxval)"""