#!/usr/bin/env python3
#-*-coding:utf-8 -*-
import re, sys
listaaa=[]
with open('aaaa.sql',encoding='utf-8') as f:
  for line in f:
    #parseip = re.search(r'(^http://www.kaixinceping.top/group1/*/.jpg$)', line)
    regular = re.compile(r'http://www.aaa.cn/group1/[^\s]*[.jpg|.png|.mp4|.mp3|.wmv]')
    parseip=re.findall(regular,line)
    if parseip == []:
      continue
    else:
      #print(parseip)
      listaaa.extend(parseip)

for a in listaaa:
  print(a)

with open('1.txt', 'w') as f:
   for i in range(len(listaaa)):
     f.write(listaaa[i]+'\r')

 # find . -name *.jpg | xargs -i cp {} /root/databack/
