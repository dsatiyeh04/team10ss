import sys

# Controller class
sys.path.append('/root/Documents/team10ss/backend/Workspace')
from Workspace import PDMLConverter

sys.path.append('/root/Documents/team10ss/backend/Analysis/PDML')
from Filter import Filter

class Controller:

    def convertPCAP(self, filename):
        foo = PDMLConverter()
        foo.convertPCAP(filename)


    def filterPDML(self, filter):
        foo = Filter()
        foo.parsePacket(filter)
