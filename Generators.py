#------------Generattor Functions--------
def gener246():
    print('Yeilding 2')
    yield 2
    print('Yeilding 4')
    yield 4
    print('Yeilding 6')
    yield 6

g = gener246()
next(g)