import time
"""
def new_time(arg=time.ctime()):
    print(arg)
#The default value are immutable.
#Here when the function is called a value has been added to the arg and when ever this function is
# called the same value would be repeating
print(new_time())
"""
#Here the arg has a default value and whene ever we teh function not_def is called without
#passing an arg then the list value will be replaced
def not_def(arg = None):
    if arg == None:
        arg = []
        arg.append(time.ctime())
        return arg

print(not_def())