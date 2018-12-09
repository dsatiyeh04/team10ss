#! /usr/bin/env python3
import sys
import xml.etree.ElementTree as et

sys.path.append('/root/Documents/team10ss/backend/Analysis/PDML')
from PDML_Manager import PDML

class Filter:
    def parsePacket(self, filter):
        pdml = PDML()
        pdmlFile = pdml.getFilename()
        print "PDML: " + pdmlFile
        tree = et.parse(pdmlFile)
        root = tree.getroot()

        for packet in root.iter('packet'):
            for proto in packet.findall('proto'):
                # for field in proto.findall('field'):
                # if protocol icmp is found
                # if proto.get('name') == 'icmp':
                #     # another for loop since you are looking inside of the protocol
                #     for field in proto.findall('field'):
                #         if field.get('showname') == 'Type: 8 (Echo (ping) request)':
                #             found = 1
                #
                #     if found == 0:
                #         packet.remove(proto)
                #
                #     # change found back to zero because then it wont read anymore packets
                #     found = 0

                if proto.get('name') != filter:
                    packet.remove(proto)
        pdml.setFilename()
        print pdml.getFilename()
        tree.write(pdml.getFilename())
# filter = Filter()
# filter.parsePacket()
