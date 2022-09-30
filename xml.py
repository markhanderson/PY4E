import xml.etree.ElementTree as ET

data = '''
<person>
   <name>Mark</name>
   <phone type="intl">
     +1 832 517 1060
    </phone>
    <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').test)
print('Attr:', tree.find('email').get('hide'))
