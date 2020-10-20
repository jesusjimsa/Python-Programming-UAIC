# Write a script that receives a URL from the command line (as argument)
# and writes the following information into a file: response status,
# response size, response type (if known), md5 hash for each fragment of
# maximum 1000 bytes of response and server response time.

import urllib2
import requests
import sys
import hashlib

if len(sys.argv) < 2:
    print("You have to provide the webpage")
    exit()

try:
    url_direction = sys.argv[1]
    webpage = urllib2.urlopen(url_direction)
    web_text = webpage.read()
except Exception as e:
    print("Error -->", e)
    exit()
else:
    print("Webpage opened correctly")

response_status = webpage.getcode()
response_size = len(web_text)
response_type = urllib2.Request(url_direction).get_type()
response_time = requests.get(url_direction).elapsed

try:
    fd = open("information.txt", 'w+')

    fd.write("Response status\n")
    fd.write(str(response_status))

    fd.write("\nResponse size\n")
    fd.write(str(response_size))

    fd.write("\nResponse type\n")
    fd.write(response_type)

    fd.write("\nResponse time\n")
    fd.write(str(response_time))

    fd.write("\nMD5\n")

    for i in range(0, len(web_text)):
        fd.write(hashlib.md5(web_text[i:i+1000]).hexdigest())
        fd.write("\n")

    fd.close()
except Exception as e:
    print("Error -->", e)
    exit()
else:
    print("All done!")
