#Dictionaries
"""
diction = dict() #creates an empty dictionary
diction["Name"] = "Satya" #Name is the key
diction["Age"] = 23
#The data willl be appended using the Keys
print(diction["Age"]) # The data is called or printed in this way
print(diction)
diction["Age"] = 22.5
print(diction)
diction["Age"] = diction["Age"] + 12
print(diction)
"""

"""
#Count the number of times a word appeared
disp = dict()
names = ["Hey","Hi","Hey","Hi",'Hello']
for name in names:
    if name not in disp:
        disp[name] = 1
    else:
        disp[name] = disp[name] + 1

print(disp)
"""

fhand_name = input("Enter name of file: ")
fhand = open(fhand_name)
num_of_times = dict()
for words in fhand:
    holder = words.rstrip().split()
    #print(holder)
    for word in holder:
        num_of_times[word] = num_of_times.get(word, 0) + 1
        #if word not in num_of_times:
        #    num_of_times[word] = 1
        #else:
        #    num_of_times[word] = num_of_times[word]+1

largest_count = None
largest_word =None
for lword, lcount in num_of_times.items():
    # The items method will return the key value pairs in a tuple like [(key,value),(key,value)]
    # So the lword and the lcount will itertate through the list of tuples and will compare
    if largest_count is None or lcount > largest_count:
        largest_count = lcount
        largest_word = lword
#print(num_of_times)
print(largest_word,largest_count)