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
    try:
        number = ''
        for tt in con:
            number += dmap[tt]
            ts = int(number)
    
    except KeyError:
        print('This is failed result')
        ts =-1
# Difference between keyerror and type error is that the key error will fetch the key 
# but type error occurs when the relevant data type argument is not passed.
# here the argument passed should be string 
    except TypeError:
        print('Type error handled :)')
        ts = -2
    return ts