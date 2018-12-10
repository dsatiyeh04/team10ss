#  _    _  _  _      _              _
# | |  | |(_)| |    | |            | |
# | |  | | _ | |  __| |  ___  __ _ | |_  ___
# | |/\| || || | / _` | / __|/ _` || __|/ __|
# \  /\  /| || || (_| || (__| (_| || |_ \__ \
#  \/  \/ |_||_| \__,_| \___|\__,_| \__||___/


import sys
import os

class PDML:
    def __init__(self):
        # Get latest session from file
         f= open("/root/Documents/team10ss/backend/Workspace/sessionCount.txt","r+")
         count = f.read()
         path = "/root/Documents/team10ss/backend/Workspace/Session_" + count.rstrip() + "/"
         dirs = os.listdir( path )
         # Get latest version number from file
         versions = open(path+"versions", "r+")
         version = versions.read()
         pdmlFile = ''
         for file in dirs:
             filename = file.split('_v')
             filename = filename[-1].split('.')
             # Get the latest PDML file
             if filename[0] == str(version.rstrip()):
                 pdmlFile = file
                 break
         self._filename = path + pdmlFile

    def getFilename(self):
        return self._filename


    def setFilename(self):
         # Get latest session from file
         f= open("/root/Documents/team10ss/backend/Workspace/sessionCount.txt","r+")
         count = f.read()
         path = "/root/Documents/team10ss/backend/Workspace/Session_" + count.rstrip() + "/"
         dirs = os.listdir( path )
         # Get latest version number from file
         versions = open(path+"versions", "r+")
         version = versions.read()
         pdmlFile = ''
         for file in dirs:
             filename = file.split('_v')
             filename = filename[-1].split('.')
             # Get the latest PDML file
             if filename[0] == str(version).rstrip():
                 pdmlFile = file
                 break
         # Increment version number
         version = int(version)+1
         versions = open(path+"versions", "w+")
         versions.write(str(version))
         pdmlFile = pdmlFile.split('_v')
         # Create new PDML file with newest version
         pdmlFile = pdmlFile[0] + "_v" + str(version) +".pdml"
         self._filename = path + pdmlFile
