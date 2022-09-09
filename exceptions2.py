#---------------Exceptions and Progammer errors-------------
# When ever a exception block is created it should not be empty
# There should be something in the exception block

import sys

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
            return int(number)
    
    except (KeyError, TypeError) as eror:
        print(f'Error type is {eror!r}', file=sys.stderr)
        raise #It will raise the error