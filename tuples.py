#Tuples
fhand = open('romeo.txt')
diction = dict()
for lines in fhand:
    words = lines.split()
    for count in words:
        diction[count] = diction.get(count, 0) + 1
#print(diction)
lst = list()
for key,val in diction.items():
    for_tuple_holding = (val, key)
    lst.append(for_tuple_holding)
#print(lst)

lst = sorted(lst, reverse = True)
#print(lst)

for val,key in lst[:10]:
    print(key,val)