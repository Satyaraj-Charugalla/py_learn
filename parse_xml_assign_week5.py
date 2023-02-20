import urllib.request as ur
import xml.etree.ElementTree as et

url = input('Enter location: ')
total_number = 0
sum = 0

print('Retrieving', url)
xml = ur.urlopen(url).read()
print('Retrieved', len(xml), 'characters')

tree = et.fromstring(xml)
counts = tree.findall('.//count')

#print(counts)
for count in counts:
    #print(count.text)
    sum = sum + int(count.text)
    total_number = total_number + 1

print('Count:', total_number)
print('Sum:', sum)