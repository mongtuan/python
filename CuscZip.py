#!/usr/bin/python
#Extract ziped file with password
import smbclient
import sys

dataServer = smbclient.SambaClient(server="172.16.160.11", share="Mat khau su dung", domain="WORKGROUP",user = sys.argv[2], password = sys.argv[3])
dataServer.chdir("2018")
with dataServer.open("MatKhau_Thang_032018.txt", "r") as passwordFile:
    for eachLine in passwordFile.readline():
        print eachLine
