#  _    _  _  _      _              _
# | |  | |(_)| |    | |            | |
# | |  | | _ | |  __| |  ___  __ _ | |_  ___
# | |/\| || || | / _` | / __|/ _` || __|/ __|
# \  /\  /| || || (_| || (__| (_| || |_ \__ \
#  \/  \/ |_||_| \__,_| \___|\__,_| \__||___/

import sys

# Controller class
sys.path.append('/root/Documents/team10ss/backend/Workspace')
from Workspace import PDMLConverter

sys.path.append('/root/Documents/team10ss/backend/Analysis/PDML')
from Filter import Filter

sys.path.append('/root/Documents/team10ss/backend/Analysis/Field')
from Tag_Manager import Tag

sys.path.append('/root/Documents/team10ss/backend/Analysis/PDML')
from PLDR import PLDR

class Controller:
    # PDML Converter from Workspace
    def convertPCAP(self, filename):
        foo = PDMLConverter()
        foo.convertPCAP(filename)

    # Filter PDML from Filter
    def filterPDML(self, filter):
        foo = Filter()
        foo.parsePacket(filter)

    # Tag Fields from Tag
    def tagFields(self, field, tagname, tagDescription):
        foo = Tag()
        foo.tagFields(field, tagname, tagDescription)

    # def createDependency(self):
    #     foo = PLDR()
    #     foo.createDependency()

    def addFieldDependency(self, fieldName):
        foo = PLDR()
        foo.addFieldDependency(fieldName)
