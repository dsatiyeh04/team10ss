#! /usr/bin/env python3
import sys
import xml.etree.ElementTree as et

sys.path.append('/root/Documents/team10ss/backend/Analysis/PDML')
from PDML_Manager import PDML

class Filter:
    def parsePacket(self, filter):
        # Get latest PDML
        pdml = PDML()
        pdmlFile = pdml.getFilename()
        tree = et.parse(pdmlFile)
        root = tree.getroot()
        # Get packets
        for packet in root.iter('packet'):
            # Get protocols
            for proto in packet.findall('proto'):
                # Remove protocols that don't match the filter
                if proto.get('name') != filter:
                    packet.remove(proto)
        # Make a new PDML file
        pdml.setFilename()
        print pdml.getFilename()
        tree.write(pdml.getFilename())
