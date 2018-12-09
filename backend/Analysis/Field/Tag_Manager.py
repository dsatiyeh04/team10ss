import os
import sys

sys.path.append('/root/Documents/team10ss/backend/Analysis/PDML')
from PDML_Manager import PDML

class Tag:
    def tagField(self, field, tagname, tagDescription):
        pdml = PDML()
        pdmlFile = pdml.getFilename()
        print "PDML: " + pdmlFile
        tree = et.parse(pdmlFile)
        root = tree.getroot()
        fields = []
        for packet in root.iter('packet'):
            for proto in packet.findall('proto'):
                for field in proto.findall('field'):
                    if field.get('name') is field:
                       field.set(tagname, tagDescription)
        pdml.setFilename()
        print pdml.getFilename()
        tree.write(pdml.getFilename())
