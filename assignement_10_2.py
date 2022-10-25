"""
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
Once you have accumulated the counts for each hour, print out the counts, sorted by hour
"""
fname = input("Enter file name: ")
fh = open(fname)
counts = dict()                                             #To chenck and increament the count of words
for line in fh:                                             
    if line.startswith('From '):
        striping = line.rstrip().split()
        hours = striping[5].split(':')[0]                   #The hours are at the 5 position in the line
        counts[hours] = counts.get(hours,0)+1               #This will check and incremet the count

lst = list()                                                
for key,val in counts.items():
    #List is created to hold the key value pairs that are generated from the counts.
    temp_tuple = (key,val)
    lst.append(temp_tuple)
    
lst.sort(reverse=False)
#This sorting will arrange the key value pairs from lowest to highest
for key,val in lst:
    print(key,val)