# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 21:00:42 2021

@author: DIAMO
"""

# from scapy.all import *

# pcap = sniff(count = 50)
# # pcap = sniff(iface = "enp9s0", count = 50)


from scapy.all import *


def capture(x): if b'HTTP/' in x.lastlayer().original and x.lastlayer().original[0:4] != b'HTTP': print('dst ip:', x.payload.dst) print('request body:', x.lastlayer().original)


def main(): sniff(filter="tcp", prn=lambda x: capture(x))


if __name__ == '__main__': main()
复制代码