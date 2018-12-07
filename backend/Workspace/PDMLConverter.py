import os


class PDMLConverter:
    def convertPCAP(self, pcap):
        self.pcap = pcap

        if pcap is None:
            print("Empty File")

        else:
            pdml = self.pcap.split('.')
            cmd = "tshark -T pdml -r " + str(self.pcap) + " > " + pdml[0] + ".pdml"
            os.system(cmd)
