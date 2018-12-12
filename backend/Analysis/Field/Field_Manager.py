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
         fieldAtt = []
         fields = []
         showname = []
         size = []
         pos = []
         show = []
         value = []
         for packet in root.iter('packet'):
             for proto in packet.findall('proto'):
                 for field in proto.findall('field'):
                     # Add field names to list
                     if field.get('name') is not None:
                         fields.append(field.get('name'))
                     if field.get('showname') is not None:
                         showname.append(field.get('showname'))
                     if field.get('size') is not None:
                         size.append(field.get('size'))
                     if field.get('pos') is not None:
                         pos.append(field.get('pos'))
                     if field.get('show') is not None:
                         show.append(field.get('show'))
                     if field.get('value') is not None:
                         value.append(field.get('value'))


         # self._showname = showname
         # self._size = size
         # self._pos = pos
         # self._show = show
         # self._value = value
         # print "-------------fields: " + str(len(fields))
         # print "-------------showname: " + str(len(showname))
         # print "-------------size: " + str(len(size))
         # print "-------------pos: " + str(len(pos))
         # print "-------------value: " + str(len(show))
         # print "-------------value: " + str(len(value))
         for i in range(len(value)):
            temp = []
            temp.append(fields[i])
            temp.append(showname[i])
            temp.append(size[i])
            temp.append(pos[i])
            temp.append(show[i])
            temp.append(value[i])
            fieldAtt.append(temp)

         self._fields = fields
         self._fieldAtt = fieldAtt

    def getFields(self):
        return self._fields

    def getShowname(self):
        return self._showname
    def getSize(self):
        return self._size
    def getPos(self):
        return self._pos
    def getShow(self):
        return self._show
    def getValue(self):
        return self._value

    def getFieldAtt(self):
        return self._fieldAtt
    # Add fields
    def setFilename(self, field):
         self._fields.append(field)
