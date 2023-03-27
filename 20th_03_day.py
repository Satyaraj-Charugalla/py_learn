#x = ' Hello '
#print(x.replace(' Hello ','Hello'))
x = [1,2,3,4,5]
y = [6,7,8,9]

x, y = y, x
print(x,y)