"""
#See how a global name is not being updated
glob = 'Hello' # Global variable
def glob_fun():
    print(glob) #Printing the variable

def update_glob_fun1(c):
    glob = c  #Trying to update using a pass by value

glob_fun()
print(update_glob_fun1(20)) 
#It will not update since the global name cannot be rebinded to another value
glob_fun()
"""

"""
glob = 'Hello' # Global variable
def glob_fun():
    print(glob) #Printing the variable

def update_glob_fun1(c):
    global glob #
    glob = c
    return glob

glob_fun()
print(update_glob_fun1(20))
"""

"""
#A tuple can be either inside a () or simply we can assign that to a variable
ab = (1,2,3,4,44)
print(ab)
pa = 1,2,3,4,5,6,7
print(type(pa))
"""

def min_max_f(items):
    return min(items),max(items)

#min_max_f((1,33,24,2324,2,0))
#print(type(min_max_f))

lower, upper = min_max_f((1,33,24,2324,2,0))
#Here we are giving 2 different values the same function with values passed into the function.
#So the first return will assign it to lower and the second return will assign to upper
print(lower)
print(upper)