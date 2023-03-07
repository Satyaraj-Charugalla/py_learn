"""
#Swap numbers
a= 10
b = 11
a, b= b, a
print(f'After Swapping a = {a} and b = {b}')
"""

"""
#Merge 2 dictionaries
x = {'a':1,'b':2}
y = {'c':11,'d':22}
z = {**x, **y}
print(f'Before merging {x} and {y}. After merging {z}')
"""

"""
#Flatenning the lists
nested_lst = [[1,2],[10,11,12]]
#flat_list = [num for sublist in nested_lst for num in sublist]
flat_list =[]
for sublist in nested_lst:
    for num in sublist:
        flat_list.append(num)
print(flat_list)
"""

"""
#List elemnts from strings to int
str_lists = ['1','2','3','4']
int_lists =[]
for strng_element in str_lists:
    int_lists.append(int(strng_element))
print(int_lists)
"""

"""
#List elemnts from strings to int
str_lists = ['1','2','3','4']
int_lists = list(map(int,str_lists))
print(int_lists)
"""

#Most comman or repeated elem in list
rep_list = [1,2,3,3,3,4,4,4,5,6,83174]
com = max(set(rep_list), key=rep_list.count)
print(com)