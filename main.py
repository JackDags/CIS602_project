# import libraries
import pyshark

# import files
from getExfil import *
from getRedunElim import *

'''
GENERAL PLAN:

1) call getExfil sending .pcap file return object list
2) call getRedunElim sending object list return object list
3) print results
'''

# start pipeline

# getting length of pre fingerprinted pcap file
# for printing purposes only
print("Counting total packets...")
print("This may take several minutes")
try:
    cap = pyshark.FileCapture('pcapFiles/FTP-Official1000.pcap')
    cap.load_packets()
    packet_amount = len(cap)
    print("Pre-fingerprinting packet amount: {}\n".format(packet_amount))
except:
    packet_amount = 36,204
    print("Pre-fingerprinting packet amount: {}\n".format(packet_amount))

# call getExfil
print("Getting Fingerprint...")
day2 = getExfil()
print("Done\n")

# print out results
print("Post Fingerprint:")
print("Amount of packets in packet list: {}\n".format(len(day2)))

# call getRedunElim
print("Redundancy Elimination...")
uniqueListDay2 = unique(day2)
print("Done\n")

# print out results
print("Post Redundancy elimination:")
print("Amount of packets in packet list: {}".format(len(uniqueListDay2)))