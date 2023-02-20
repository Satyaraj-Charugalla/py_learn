import xml.etree.cElementTree as ET

data = '''
<person>
    <name>Satya</name>
    <phone type="intl">
        44 55 22 22
    </phone>
    <email hide="yes"/>
</person>
'''

tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))