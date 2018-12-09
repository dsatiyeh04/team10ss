#  _    _  _  _      _              _
# | |  | |(_)| |    | |            | |
# | |  | | _ | |  __| |  ___  __ _ | |_  ___
# | |/\| || || | / _` | / __|/ _` || __|/ __|
# \  /\  /| || || (_| || (__| (_| || |_ \__ \
#  \/  \/ |_||_| \__,_| \___|\__,_| \__||___/


import os
import sys


class PDMLConverter:
    def convertPCAP(self, pcap):
        self.pcap = pcap

        if pcap is None:
            print("Empty File")

        else:
            # Read the session number
            f= open("/root/Documents/team10ss/backend/Workspace/sessionCount.txt","r+")
            count = f.read()
            path = "/root/Documents/team10ss/backend/Workspace/Session_" + count.rstrip() + "/"
            # If session already exists, increment session number and create new directory with new number
            if(os.path.isdir(path)):
                count = int(count)+1
                path = "/root/Documents/team10ss/backend/Workspace/Session_" + str(count).rstrip() + "/"
                os.mkdir(path)
                versions = open(path+"versions", "w+")
                # Start version file with version numbers
                versions.write("1")
                f= open("/root/Documents/team10ss/backend/Workspace/sessionCount.txt","w+")
                f.write(str(count))
            else:
                os.mkdir(path)
                # Start version file with version numbers
                versions = open(path+"versions", "w+")
                versions.write("1")
            pdml = self.pcap.split('/')
            pdml = pdml[-1].split('.')
            versions = open(path+"versions", "r+")
            version = versions.read()
            pdmlFile = path + pdml[0] + "_v"+version + ".pdml"
            # Convert pcap and write into new PDML file
            cmd = "tshark -T pdml -r " + str(self.pcap) + " > " + pdmlFile
            os.system(cmd)
