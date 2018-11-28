import os


class PDMLConverter:
    def convertPCAP(self, pcap):
        self.pcap = pcap

        if pcap is None:
            print("Empty File")

        else:

            cmd = "tshark -T pdml -r " + self.pcap + " > test.pdml"
            os.system(cmd)

foo = PDMLConverter()
foo.convertPCAP("abis-accept-network.pcap")
