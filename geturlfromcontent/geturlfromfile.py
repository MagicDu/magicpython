#!/usr/bin/env python3
#-*-coding:utf-8 -*-
import re, sys,os
from os import path
from urllib.parse import urlparse

# 从文件中提取路径
def get_url_from_file(file_path):
    urls=[]
    files=os.listdir(file_path)
    for fi in files:
        fileurl=path.join(file_path,fi)
        print(fileurl)
        with open(fileurl,encoding='utf-8') as f:
            for line in f:
                regular = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
                parseurl=re.findall(regular,line)
                if parseurl == []:
                    continue
                else:
                    urls.extend(parseurl)
    return urls
#url 写入 txt
def deal_url2file(urls):
    with open('1.txt', 'w') as f:
        for i in range(len(urls)):
           url=urls[i].replace("',","")
           parsed_uri = urlparse(url)
           rep='{probuf.scheme}://{host.netloc}'.format(probuf=parsed_uri, host=parsed_uri)
           url=url.replace(rep,'/app')
           f.write(url+'\r')

def main():
    urls=get_url_from_file("C:\\Users\\magicdu\\Desktop\\sql")
    deal_url2file(urls)
 
if __name__ == '__main__':
    main()


