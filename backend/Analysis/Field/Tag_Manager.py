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
class Tag:
    def tagField(self, taggedField, tagName, tagDescription):
        # Get the latest PDML
        pdml = PDML()
        pdmlFile = pdml.getFilename()
        tree = et.parse(pdmlFile)
        root = tree.getroot()
        # Get packets
        for packet in root.iter('packet'):
            # Get protocols
            for proto in packet.findall('proto'):
                # Get fields
                for field in proto.findall('field'):
                    if field.get('name') == taggedField:
                        # Create new tag
                        field.set(tagName, tagDescription)
        # Make a new PDML file
        pdml.setFilename()
        tree.write(pdml.getFilename())
