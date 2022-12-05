import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://py4e.org/romeo.txt')
count = 0
for line_count in fhand:
    print(line_count.decode().strip())
    count = count +1

print(count)