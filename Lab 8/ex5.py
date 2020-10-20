# Write a script that receives a URL from the command line (as an argument) and
# downloads all images (img src) to the current directory.

import urllib2
import re
import sys

if len(sys.argv) < 2:
    print("You have to provide the webpage")
    exit()

images_list = list()
image_name = 0

try:
    url_direction = sys.argv[1]
    webpage = urllib2.urlopen(url_direction).read()
except Exception as e:
    print("Error -->", e)
    exit()
else:
    print("Webpage opened correctly")


re_image = re.compile(r"(<img .* src=\")(.*\.jpg|.*\.png|.*\.tiff|.*\.jpeg|.*\.gif|.*\.bmp)(\".*)")
re_extension = re.compile(r"(.*)(\.jpg|\.png|\.tiff|\.jpeg|\.gif|\.bmp)")

try:
    for found in re_image.finditer(webpage):
        image = found.group(2)
        images_list.append(image)

        print("\033[92mFound\033[0m", image)

        img_parts = re_extension.search(image)
        img_extension = img_parts.group(2)

        fd = open(str(image_name) + img_extension, "w+")
        fd.write(urllib2.urlopen(image).read())
        fd.close()

        image_name += 1
except Exception as e:
    print("Error -->", e)
    exit()
else:
    print(len(images_list), "images found and downloaded")
