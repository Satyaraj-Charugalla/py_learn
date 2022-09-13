#-----------------------Lists and set comprehensions-----------------
words = 'This is some randomly generated text for knowing what is the List and set comprehensions'.split()
print(words)


# Syntax for the comprehensions is 
# [expr(item) for item in iterable] Iterable is the variable that holds value
print([len(word) for word in words])