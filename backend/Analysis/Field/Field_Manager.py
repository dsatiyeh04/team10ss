#  _    _  _  _      _              _
# | |  | |(_)| |    | |            | |
# | |  | | _ | |  __| |  ___  __ _ | |_  ___
# | |/\| || || | / _` | / __|/ _` || __|/ __|
# \  /\  /| || || (_| || (__| (_| || |_ \__ \
#  \/  \/ |_||_| \__,_| \___|\__,_| \__||___/

import os
import sys

sys.path.append('/root/Documents/team10ss/backend/Analysis/PDML')
from PDML_Manager import PDML

import xml.etree.ElementTree as et
# Get all field names
class Field:
    def __init__(self):
        # Get latest PDML
         pdml = PDML()
         pdmlFile = pdml.getFilename()
         tree = et.parse(pdmlFile)
         root = tree.getroot()
         # Create list to store all field names
         fields = []
         for packet in root.iter('packet'):
             for proto in packet.findall('proto'):
                 for field in proto.findall('field'):
                     # Add field names to list
                     if field.get('name') is not None:
                        fields.append(field.get('name'))
         self._fields = fields

    def getFields(self):
        return self._fields

    # Add fields
    def setFilename(self, field):
         self._fields.append(field)
