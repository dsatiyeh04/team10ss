import os
import sys

sys.path.append('/root/Documents/team10ss/backend/Analysis/PDML')
from PDML_Manager import PDML

import xml.etree.ElementTree as et

class Field:
    def __init__(self):
         pdml = PDML()
         pdmlFile = pdml.getFilename()
         print "PDML: " + pdmlFile
         tree = et.parse(pdmlFile)
         root = tree.getroot()
         fields = []
         for packet in root.iter('packet'):
             for proto in packet.findall('proto'):
                 for field in proto.findall('field'):
                     if field.get('name') is not None:
                        fields.append(field.get('name'))
         self._fields = fields

    def getFields(self):
        return self._fields

    def setFilename(self, field):
         self._fields.append(field)
