#!/usr/bin/python
import os
import urllib
import re

link = "http://www.cuscsoft.com"
web = urllib.urlopen(link)
#Get web address content
content = web.read()
#Filt web address only
host = re.findall(r'(?:[a-zA-z0-9]+\.){2,}(?:[a-zA-Z]{2,3})',str(content))

for eachH in host:
    print eachH
    #Find ip every found host
    os.system("host "+eachH)
