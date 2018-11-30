import os


class PDMLConverter:
    def convertPCAP(self, pcap):
        self.pcap = pcap

        if pcap is None:
            print("Empty File")

        else:

            cmd = "tshark -T pdml -r " + self.pcap +".pcap" + " > " + self.pcap + ".pdml"
            os.system(cmd)
