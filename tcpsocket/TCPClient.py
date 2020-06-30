#!/usr/bin/env python3
# -*-coding:utf-8 -*-
from socket import *
serverName='192.168.1.107'
severPort=12000
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,severPort))
message=input('input lowercase sentence:')
clientSocket.send(message.encode())
modifiedSentence=clientSocket.recv(1024)
print(modifiedSentence.decode())
clientSocket.close()
