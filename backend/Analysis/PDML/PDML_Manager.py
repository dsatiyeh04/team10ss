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
             # print file
             filename = file.split('_v')
             filename = filename[-1].split('.')
             # print "version: " + version
             if filename[0] == str(version.rstrip()):
                 # print "THIS SHOULD PRINTTTTTTTTTTTTTT"
                 pdmlFile = file
                 break
         self._filename = path + pdmlFile

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
             print "file: " + file
             filename = file.split('_v')
             filename = filename[-1].split('.')
             print "filename[0]: " + filename[0]
             print "version: " + version
             if filename[0] == str(version).rstrip():
                 print "PRINT PLEEEEAASSSEEEE"
                 pdmlFile = file
                 print pdmlFile
                 break
         version = int(version)+1
         versions = open(path+"versions", "w+")
         versions.write(str(version))
         pdmlFile = pdmlFile.split('_v')
         print "pdmlFile[0]: " + pdmlFile[0]
         pdmlFile = pdmlFile[0] + "_v" + str(version) +".pdml"
         print "pdmlFile: " + pdmlFile
         self._filename = path + pdmlFile

p = PDML()
