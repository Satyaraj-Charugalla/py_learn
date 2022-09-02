#--------------------Functions-------------------
"""
def additionn(y):
    return y*y

print(additionn(10))
"""

""" 
#This function has multiple parameters involved hence we will 
#pass the similar number of arguments when calling the function
def nth_root(rad, n):
    return rad ** (1/n)

print(nth_root(27,3))
"""

#When we don't know the number of args passed and we need only a limited number
#then we can give a * before the parameter
def arbi_func(*param):
    print('This is an arbitary function')
    x = param[2] * param[1] # here we have taken the 2nd and the 1st arguments
    print(x)

arbi_func(10,11,12)