# Implement a client for the server developed at 2a: a script that receives
# from the command line an addr string, a port integer, and a string msg,
# and sends a UDP packet to the addr address, the port port, and the msg
# content.

import sys
import socket

try:
	addr = sys.argv[1]
	port = int(sys.argv[2])
	msg = sys.argv[3]
except:
	print "You need to write three arguments: <server_addres> <port> <message>"
	sys.exit(1)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(msg, (addr, port))