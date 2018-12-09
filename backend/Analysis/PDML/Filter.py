#! /usr/bin/env python3
import sys
import xml.etree.ElementTree as et

sys.path.append('/root/Documents/team10ss/backend/Analysis/PDML')
from PDML_Manager import PDML

class Filter:
    def parsePacket(self):
        pdml = PDML()
        pdmlFile = pdml.getFilename()
        tree = et.parse(pdmlFile)
        root = tree.getroot()
        found = 0

        for packet in root.iter('packet'):
            for proto in packet.findall('proto'):
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

                if proto.get('name') != 'icmp':
                    packet.remove(proto)
        f= open("/root/Documents/team10ss/backend/Workspace/sessionCount.txt","r+")
        count = f.read()
        path = "/root/Documents/team10ss/backend/Workspace/Session_" + count.rstrip() + "/"
        # dirs = os.listdir( path )
        versions = open(path+"versions", "r+")
        version = versions.read()
        version = int(version)+1
        versions = open(path+"versions", "w+")
        versions.write(str(version))
        pdmlFile = pdmlFile.split('_v')

        pdmlFile = pdmlFile[0] + "_v" + str(version) +".pdml"
        tree.write(pdmlFile)
        # pdmlFile = setFilename()
filter = Filter()
filter.parsePacket()
