# Implement using the socket module (TCP), a server that writes when a client
# connects to it the following data: the connection time in human-readable
# format, the address, and the port of the client.

import time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 2024))
s.listen(1)

while True:
	print "Waiting for a client..."
	(connection, address) = s.accept()

	print "Connect address:", address
	print "Port: 2024"
	print (time.strftime("%H:%M:%S")), (time.strftime("%d/%m/%Y"))

	connection.close()