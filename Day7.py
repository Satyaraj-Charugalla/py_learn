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