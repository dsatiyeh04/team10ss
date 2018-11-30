import xml.etree.ElementTree as et

tree = et.parse('output2.pdml')

root = tree.getroot()

found = 0

for packet in root.iter('packet'):
    for proto in packet.findall('proto'):
        if proto.get('name') == 'icmp':
            for field in proto.findall('field'):
                if field.get('showname') == 'Type: 8 (Echo (ping) request)':
                    field.set('tag', 'TEST')

tree.write("tagTest.pdml")
