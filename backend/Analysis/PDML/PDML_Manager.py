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
         f= open("/root/Documents/team10ss/backend/Workspace/sessionCount.txt","r+")
         count = f.read()
         path = "/root/Documents/team10ss/backend/Workspace/Session_" + count.rstrip() + "/"
         dirs = os.listdir( path )
         versions = open(path+"versions", "r+")
         version = versions.read()
         pdmlFile = ''
         for file in dirs:
             filename = file.split('_v')
             filename = filename[-1].split('.')
             if filename[0] == str(version):
                 # print "THIS SHOULD PRINTTTTTTTTTTTTTT"
                 pdmlFile = file
                 break
         self._filename = pdmlFile

    def getFilename(self):
        return self._filename

    def setFilename(self):
         f= open("/root/Documents/team10ss/backend/Workspace/sessionCount.txt","r+")
         count = f.read()
         path = "/root/Documents/team10ss/backend/Workspace/Session_" + count.rstrip() + "/"
         dirs = os.listdir( path )
         versions = open(path+"versions", "r+")
         version = versions.read()
         pdmlFile = ''
         for file in dirs:
             filename = file.split('_v')
             filename = filename[-1].split('.')
             if filename[0] == str(version):
                 print "THIS SHOULD PRINTTTTTTTTTTTTTT"
                 pdmlFile = file
                 break
         self._filename = pdmlFile

p = PDML()
print p.getx()
