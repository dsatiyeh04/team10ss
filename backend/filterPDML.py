#! /usr/bin/env python3

import xml.etree.ElementTree as et

tree = et.parse('ipv4frags.pdml')

root = tree.getroot()

found = 0

for packet in root.iter('packet'):
    for proto in packet.findall('proto'):
        # if proto.get('name') != 'lapd':
        # packet.remove(proto)

        if proto.get('name') == 'icmp':
            for field in proto.findall('field'):
                if field.get('showname') == 'Type: 8 (Echo (ping) request)':
                    found = 1

            if found == 0:
                packet.remove(proto)

            found = 0

        if proto.get('name') != 'icmp':
            packet.remove(proto)

tree.write("output2.pdml")
