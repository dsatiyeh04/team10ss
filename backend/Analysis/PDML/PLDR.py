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
class PLDR:
    def createDependency(self):
        # Get the latest PDML
        pdml = PDML()
        pdmlFile = pdml.getFilename()
        tree = et.parse(pdmlFile)
        root = tree.getroot()
        newElement = et.Element("dependency")
        root.append(newElement)
        # Make a new PDML file
        pdml.setFilename()
        tree.write(pdml.getFilename())

    def addFieldDependency(self, fieldname):
        pdml = PDML()
        pdmlFile = pdml.getFilename()
        tree = et.parse(pdmlFile)
        root = tree.getroot()
        # Get packets
        dep = root.find("dependency")
        if(dep is None):
            newElement = et.Element("dependency")
            root.append(newElement)
            dep = root.find("dependency")
            field = et.SubElement(dep, "field")
            field.set("name", fieldname)
        else:
            field = et.SubElement(dep, "field")
            field.set("name", fieldname)
        # Make a new PDML file
        pdml.setFilename()
        tree.write(pdml.getFilename())
