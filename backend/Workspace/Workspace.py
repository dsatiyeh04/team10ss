import os


class PDMLConverter:
    def convertPCAP(self, pcap):
        self.pcap = pcap

        if pcap is None:
            print("Empty File")

        else:
            f= open("/root/Documents/team10ss/backend/Workspace/sessionCount.txt","r+")
            count = f.read()
            path = "/root/Documents/team10ss/backend/Workspace/session" + count.rstrip() + "/"
            if(os.path.isdir(path)):
                count = int(count)+1
                path = "/root/Documents/team10ss/backend/Workspace/session" + str(count).rstrip() + "/"
                os.mkdir(path)
                f= open("/root/Documents/team10ss/backend/Workspace/sessionCount.txt","w+")
                f.write(str(count))
            else:
                os.mkdir(path)
            pdml = self.pcap.split('/')
            pdml = pdml[-1].split('.')
            cmd = "tshark -T pdml -r " + str(self.pcap) + " > " + path + pdml[0] + ".pdml"
            os.system(cmd)
