"""
x = 'From marquard@uct.ac.za'
print(x[8])

x = '40'
y = int(x) + 2
print(y)

x = 'From marquard@uct.ac.za'
print(x[14:17])

greet = 'Hello Bob'
print(greet.upper())

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])
"""

text = "X-DSPAM-Confidence:    0.8475"
x = text.find("    ")
#print(x)
val = text[x+1:]
z = float(val)
#print(type(z))
print(z)