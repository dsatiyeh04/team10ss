#! /usr/bin/env python3

import xml.etree.ElementTree as et


class filterPDML:
    def parsePacket(self, pcap):
        tree = et.parse(pcap)
        root = tree.getroot()
        found = 0

        for packet in root.iter('packet'):
            for proto in packet.findall('proto'):
                # if protocol icmp is found
                if proto.get('name') == 'icmp':
                    # another for loop since you are looking inside of the protocol
                    for field in proto.findall('field'):
                        if field.get('showname') == 'Type: 8 (Echo (ping) request)':
                            found = 1

                    if found == 0:
                        packet.remove(proto)

                    # change found back to zero because then it wont read anymore packets
                    found = 0

                if proto.get('name') != 'icmp':
                    packet.remove(proto)

        tree.write("output3.pdml")


foo = filterPDML()
foo.parsePacket('ipv4frags.pdml')