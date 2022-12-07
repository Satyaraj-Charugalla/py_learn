import requests

count = 0 
res = requests.get('http://data.py4e.org/romeo.txt')
for lines in res:
    print(lines.decode().strip())
    count = count +1

print(count)