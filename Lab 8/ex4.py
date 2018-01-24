# Once the server from 3 is started, extract the .txt file names and write to the console.

import urllib2
import SimpleHTTPServer
import SocketServer
import re
# import pdb; pdb.set_trace()

urlDirectory = "http://127.0.0.1:9000"
page = urllib2.urlopen(urlDirectory).read()

r = re.compile("(<li><a href=)\"([^\"\.]*\.txt)\">.*([A-Za-z\.\s,]+)<\/a>")

try:
	for found in r.finditer(page):
		textFile = found.group(2)

		fileURL = "http://127.0.0.1:9000/" + textFile

		fileContent = urllib2.urlopen(fileURL).read()

		print '\033[92m', textFile, '\033[0m'	# Green
		print fileContent
except Exception as e:
	print "Error ->", e