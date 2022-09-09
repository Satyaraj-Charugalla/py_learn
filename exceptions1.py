#-----------------Handling exceptions and the workflow of the exceptions-----------------
dmap={
    'zero':'0',
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7'
}

def to_convert(con):
    ts = -1
    try:
        number = ''
        for tt in con:
            number += dmap[tt]
            ts = int(number)
    
    except KeyError:
        print('This is failed result')
        #ts =-1
# Difference between keyerror and type error is that the key error will fetch the key 
# but type error occurs when the relevant data type argument is not passed.
# here the argument passed should be string 
    except TypeError:
        print('Type error handled :)')
        #ts = -2
# When declaring an exception if the type of exception is not mentioned then all 
# kinds of execptions will be handled
    return ts