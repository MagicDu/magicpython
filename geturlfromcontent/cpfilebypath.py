#!/usr/bin/env python3
#-*-coding:utf-8 -*-
from shutil import copyfile
import re, sys,os

def copybyurl():
    newbasepath="/app/ai/"
    with open('1.txt', 'r') as f:
        urls=f.readlines()
        for i in  range(len(urls)):
            oldurl=urls[i].replace('\r','').replace('\n','')
            newurl=oldurl.replace("/app/",newbasepath)
            dir=os.path.dirname(newurl)
            if not os.path.exists(dir):
                os.makedirs(dir)
            print(newurl,"复制中------------",i)
            copyfile(oldurl,newurl)

def main():
    copybyurl()
 
if __name__ == '__main__':
    main()
