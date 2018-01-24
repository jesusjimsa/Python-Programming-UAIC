# Start a server to expose the files and directories in the current directory.
# Access that server from a browser, and then using a python HTTP client
# (urllib.request)

import urllib2
import SimpleHTTPServer
import SocketServer

httpd = SocketServer.TCPServer(("127.0.0.1", 9000), SimpleHTTPServer.SimpleHTTPRequestHandler)

httpd.serve_forever()