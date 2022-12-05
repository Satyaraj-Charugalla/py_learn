import urllib.request
"""
fhand = urllib.request.urlopen('http://py4e.org/romeo.txt')
count = 0
for line_count in fhand:
    print(line_count.decode().strip())
    count = count +1

print(count)
"""

with urllib.request.urlopen('http://py4e.org/romeo.txt') as response:
    fhand = response.read()
    count = 0
    for line_count in fhand:
        print(line_count.decode().strip())
        count = count +1

print(count)