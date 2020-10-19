from scapy.all import *
import sys

host=sys.argv[1]
ttl = 1
print("Tracing route to "+host);

while ttl < 200:
    ipLayer = IP()
    ipLayer.dst = host #set destination host
    ipLayer.ttl = ttl #set TTL for packet
    ICMPpkt = ICMP()
    pkt = ipLayer/ICMPpkt
    reply = sr1(pkt, verbose = 0, timeout=5) #send packet and wait for reply
    
    if (reply is None):
        print("Timeout")
        ttl+=1
    elif (reply[ICMP].type == 0):
        print(reply[IP].src+" is "+str(ttl)+" hops away")
        print("Done")
        break
    elif (reply[ICMP].code == 0 and reply[ICMP].type == 11):
        print(reply[IP].src+" is "+str(ttl)+" hops away")
        ttl+=1
