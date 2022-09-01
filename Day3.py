#This will have all the code practices that are done in day 2
#----------------------Collection Types----------------------
"""
from urllib.request import urlopen
story = urlopen('http://sixty-north.com/c/t.txt')
story_words = []
for line in story:
    line_words=line.decode('utf-8').split()
    for word in line_words:
        story_words.append(word)
story.close()

for words in story_words:
    print(words)

"""

#Strings
#b = "Hello, World!"
#print(b[-5:-2])
#print(b[2:])
#print(b[:4])
#print(b.split(","))  # this is the split function

#------------------Format Function-------------------
#age = 36
#txt = "My name is John, and I am {}"
#print(txt.format(age))

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders
"""
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
"""

#The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."
print(txt)