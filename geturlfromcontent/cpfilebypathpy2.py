#!/usr/bin/env python2
#-*-coding:utf-8 -*-
from shutil import copyfile
import re, sys,os
sys.setrecursionlimit(1000000)
def copybyurl():
    newbasepath="/root/app/static/"
    with open('1.txt', 'r') as f:
        urls=f.readlines()
        for i in  range(len(urls)):
            oldurl=urls[i].replace('\r','').replace('\n','')
            newurl=oldurl.replace("/root/prostatic/",newbasepath)
            dir=os.path.dirname(newurl)
            if not os.path.exists(dir):
                os.makedirs(dir)
            print(newurl,"coping------------",i)
            try:
                copyfile(oldurl,newurl)
            except:
                print("error")

def main():
    copybyurl()
 
if __name__ == '__main__':
    main()
