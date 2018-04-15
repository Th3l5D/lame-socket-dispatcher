import socket
import sys

if len(sys.argv) > 1:

    dest_ip = socket.gethostbyname(sys.argv[1])
    resp_ip = ''
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    response = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    # we need to open raw socket in order to get ICMP responses. I didn't find a way to get them without that.
    ttl = 1
    while resp_ip != dest_ip:
        sock.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        sock.sendto(b"", (dest_ip, 33434))
        # actually, the port is not random, some firewalls check it to autorize traceroute packets. I checked the traceroute source & stole the port :)
        resp_ip = response.recvfrom(1024)[1][0]
        print(str(ttl)+' '+resp_ip)
        ttl+=1

else:
    print('I think you\'re a bit dump. You forgot the destination address')