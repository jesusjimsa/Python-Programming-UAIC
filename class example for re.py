import os, sys, re
from stat import *

s = "ana  has appleS"
m2 = re.search(".*?(\w+)", s)

if m2:
    print(m2.group(0))
    print(m2.group(1))

m3 = re.match(".*?(\w+)", s)

if m2:
    print(m3.group(0))
    print(m3.group(1))

m4 = re.findall("(\w+)", s)

if m4:
    print(m4)

m5 = re.split("\W", s)

if m5:
    print(m5)