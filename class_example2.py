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

class Aircaft:
    def __init__(self,plane_name,plane_model,num_of_seats,num_of_rows):
        self._plane_name = plane_name
        self._plane_model = plane_model
        self._num_of_seats = num_of_seats
        self._num_of_rows = num_of_rows
    
    def plane_name(self):
        return self._plane_name
    
    def plane_model(self):
        return self._plane_model

    def seating_plan(self):
        return (range(1,self._num_of_seats + 1),'ABCDEF'[:self._num_of_rows])