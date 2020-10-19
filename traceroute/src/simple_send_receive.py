from scapy.all import *
import sys

host=sys.argv[1]
ttl = 200
print("Sending packet to "+host);

ipLayer = IP()
ipLayer.dst = host #set destination host
ipLayer.ttl = ttl #set TTL for packet
ICMPpkt = ICMP()
pkt = ipLayer/ICMPpkt
reply = sr1(pkt, verbose = 0) #send packet and wait for reply
print("Reply: Type:",reply[ICMP].type, "Source:"+reply[IP].src)
