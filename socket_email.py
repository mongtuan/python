#!/usr/bin/python
import socket
import sys

if len(sys.argv) != 2:
    print "Usage: socket_email.py <username>"
    sys.exit(0)
#Create socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect

connect = s.connect(('gmail-smtp-in.l.google.com',25))

#Receive the banner

banner = s.recv(1024)
print banner

s.send('VRFY ' + sys.argv[1] + '\r\n')

result = s.recv(1024)
print result 
s.close()
