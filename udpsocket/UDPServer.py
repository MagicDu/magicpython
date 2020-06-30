#!/usr/bin/env python3
# -*-coding:utf-8 -*-
from socket import *
severPort=12000
serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',severPort))
print('the server is ready to receive')
while True:
    message,clientAddress=serverSocket.recvfrom(2048)
    print('receive from',clientAddress,'message:',message.decode())
    modifiedMessage=message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(),clientAddress)
