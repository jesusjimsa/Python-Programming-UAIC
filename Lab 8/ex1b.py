# Implement a client for the server developed at 1a: a script that receives
# from the command line a string addr and an integer port and connects
# through TCP to the addr address at the port port.

import socket
import sys

try:
    addr = sys.argv[1]
    port = int(sys.argv[2])
except OSError:
    print("You need to write two arguments: <server_addres> <port>")
    sys.exit(1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((addr, port))
s.close()
