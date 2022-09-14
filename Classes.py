# Class syntax => 
# class <name>:
"""
#Model for aircraft flights
class Flights:
    pass
"""

class marks:
    def __init__(aaa,m1,m2,m3):
        aaa.m1 = m1
        aaa.m2 = m2
        aaa.m3 = m3
    
    def avg(aaa):
        return (aaa.m1+aaa.m2+aaa.m3)/3

    def sum(aaa):
        return aaa.m1+aaa.m2+aaa.m3


stud1 = marks(20,40,60)
stud2 = marks(80,10,60)

print (f'The avergae of the 2 students is {(stud1.sum()+stud2.sum())/2}')
#print (f'The sum of the marks is {stud1.avg()}')
#print (f'The sum of the marks is {stud1.sum()}')