# Implement using the socket module (UDP), a server that when is receiving a UDP
# packet (datagram) writes in a text file the following information: time and
# date, address, port, length, md5 hash of the content in hex format, sha256.

import socket
import time
import hashlib

addr = "127.0.0.1"
port = 2024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((addr, port))

fd = open("result.txt", 'w')

(data, address) = s.recvfrom(2048)
datetime = (time.strftime("%H:%M:%S")) + " " + (time.strftime("%d/%m/%Y"))
msgLen = len(data)
md5 = hashlib.md5(data).hexdigest()
sha256 = hashlib.sha256(data).hexdigest()

fd.write("Message sent:\n")
fd.write(str(data))
fd.write("\n\nDate and time:\n")
fd.write(datetime)
fd.write("\n\nAddress:\n")
fd.write(str(addr))
fd.write("\n\nPort:\n")
fd.write(str(port))
fd.write("\n\nMessage's length:\n")
fd.write(str(msgLen))
fd.write("\n\nMD5 hash:\n")
fd.write(md5)
fd.write("\n\nSHA256 hash:\n")
fd.write(sha256)