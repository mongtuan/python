#!/usr/bin/python
import os
import urllib
import re

link = "http://www.cuscsoft.com"
web = urllib.urlopen(link)
content = web.read()
host = re.findall('(www)?\.([a-zA-z0-9]+\.)+',content)
print host[0]
