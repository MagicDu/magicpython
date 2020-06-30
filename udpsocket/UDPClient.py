#!/usr/bin/env python3
# -*-coding:utf-8 -*-
from socket import *
serverName='192.168.1.107'
severPort=12000
clientSocket=socket(AF_INET,SOCK_DGRAM)
message=input('input lowercase sentence:')
clientSocket.sendto(message.encode(),(serverName,severPort))
modifiedMessage,serverAddress=clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
