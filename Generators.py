#------------Generattor Functions--------
def take(count,iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter =+ 1
        yield item


def distinc(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)

def pipe():
    items = [3,6,9,22,34,12,22,3,6]
    for item in take(3,distinc(items)):
        print(item)

pipe()