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
    number = ''
    for tt in con:
        number += dmap[tt]
        ts = int(number)
    
    return ts