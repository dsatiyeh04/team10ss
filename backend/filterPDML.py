#! /usr/bin/env python3

import xml.etree.ElementTree as et

tree = et.parse('test.pdml')

root = tree.getroot()

for packet in root.iter('packet'):
    for proto in packet.findall('proto'):
        if proto.get('name') != 'lapd':
            packet.remove(proto)

tree.write("output.pdml")
