
import xml.etree.ElementTree as ET

data = '''
    <stuff>
        <users>
            <user x="2">
              <id>001</d>
              <name>Mark</name>
        </user>
        <user x="7">
              <id>009</id>
              <name>Stephanie</name>
            </user>
        </users>
    </stuff>'''

stuff = ET.fromstring(input)
lst - stuff.findall('user/user')
print('User count:', len(list))

for item in lst:
        print('Name', item.find('name').text)
        print('Id', item.find('id').text)
        print('Attribute', item.get("x"))
