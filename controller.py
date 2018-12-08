import sys

# Controller class
sys.path.append('/root/Documents/team10ss/backend/Workspace')
from PDMLConverter import PDMLConverter


class Controller:

    def convertPCAP(self, filename):
        foo = PDMLConverter()
        foo.convertPCAP(filename)
