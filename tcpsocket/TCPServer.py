#!/usr/bin/env python3
# -*-coding:utf-8 -*-
from socket import *
severPort=12000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',severPort))
serverSocket.listen(1)
print('the server is ready to receive')
while True:
    connectionSocket,addr=serverSocket.accept()
    sentence=connectionSocket.recv(1024).decode()
    print('receive from',addr,'message:',sentence)
    capitalizedSentence=sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
