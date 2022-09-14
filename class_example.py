#Model for aircraft flights
class Flights:

    #def flight_number(abc): #abc is a self
     #   return 'AB090909'
    def __init__(self,fnumber):
        if not fnumber[:2].isalpha():
            raise ValueError(f'Invalid air code {fnumber}')
        
        if not fnumber[:2].isupper():
            raise ValueError(f'Invalid air code {fnumber}')
        
        if not (fnumber[2:].isdigit() and fnumber[2:] < '9999'):
            raise ValueError(f'Invalid air code {fnumber}')
        self._flight_number = fnumber
    
    def flight_number(self):
        return self._flight_number

fn = Flights('AH3333')
print(f'The flight number is {fn.flight_number()}')