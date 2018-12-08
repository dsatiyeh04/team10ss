import os


class PDMLConverter:
    def convertPCAP(self, pcap):
        self.pcap = pcap

        if pcap is None:
            print("Empty File")

        else:
	    sessionFolder = "mkdir Session"
	    os.mkdir("/root/Documents/team10ss/backend/Workspace/session")
            pdml = self.pcap.split('/')
	    pdml = pdml[-1].split('.')
            cmd = "tshark -T pdml -r " + str(self.pcap) + " > /root/Documents/team10ss/backend/Workspace/session/" + pdml[0] + ".pdml"
            os.system(cmd)
