"""
eurfloor = int(input('Europe floor:'))
usfloor = eurfloor + 1
print('US Floor is',usfloor)


x = 98.6
print(int(x))


def tolearn_return(altt):
    if altt == 'A':
        return 'Hello there!'
    elif altt == 'B':
        return 'Hey There!'
    else:
        return 'Shoot :/'
"""

"""
hrs = float(input("Enter Hours:"))
rate = float(input("Enter Pay:"))
def computepay(h, r):
    if h > 40:
        regu = float(h * r)
        ovt = float((1.5 * r)*(h - 40))
        #tot = regu + ovt
        return regu + ovt
    else:
        return h*r

p = computepay(hrs, rate)
print("Pay", p)
"""

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Pay:"))
if hrs > 40:
    def computepay(h = hrs, r = rate):
        regu = float(h * r)
        ovt = float((1.5 * r)*(h - 40))
        #tot = regu + ovt
        return regu + ovt

else:
    print(hrs*rate)


p = computepay()
print("Pay", p)

x = hrs*rate
print(x)
y = (hrs - 40) * (1.5 * rate)
print(y)
z = x + y
print(z)