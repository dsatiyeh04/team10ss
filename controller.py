import sys

sys.path.append('/root/Documents/team10ss/backend/')
from PDMLConverter import PDMLConverter


class Controller:

    def convertPCAP(self, filename):
        foo = PDMLConverter()
        foo.convertPCAP(filename)
