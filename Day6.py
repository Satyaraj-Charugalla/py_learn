"""
#The main objective is to show that the variables are immutebale
#which means that if a variable is binded with a value and later it is updated the 
#variable will be refering to the new value and the old value will be trashed...Not replaced
x = 10
y = x #here the value y will be pointing out to the value of x which is 10
x = 25 #now the value of x is updated.
#Now the value 10 will not be trashed out coz Y is refering to it
print('Value of X is :',x)
print('Value of Y is :',y)
"""

#But when a list is assigned then the value will be replaced
#When a list is binded to a varible, then the list values can be replaced
xx = [22,23,24,29]
yy = xx
print(yy)
yy[1] = 1 #When a value inside the list is changed from a reference variable(yy), 
#even then also the value gets replaced and xx will refer to the new list
print(yy)