#-----------------------Lists and set comprehensions-----------------
"""
words = 'This is some randomly generated text for knowing what is the List and set comprehensions'.split()
print(words)
"""

# Syntax for the list comprehensions is 
# [expr(item) for item in iterable] Iterable is the variable that holds value
# print([len(word) for word in words])

from math import sqrt
def is_prime(x):
    if x < 2:
        return False
    for i in range(2,int(sqrt(x)) +1):
        if x % i == 0:
            return False
        return i
print ([x for x in range(101) if is_prime(x)])