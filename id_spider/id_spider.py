#!/usr/bin/env python3
# -*-coding:utf-8 -*-
import requests
import os
import bs4
import base64
from urllib.request import urlretrieve
import pymysql
import threading

## 用户对象
class Person(object):
    def __init__(self,name,id_number,id_front,id_back,driving_license):
        self.name = name
        self.id_number=id_number
        self.id_front=id_front
        self.id_back=id_back
        self.driving_license=driving_license


# 下载图片
def get_image(dir_name,image_url, image_name):
    os.makedirs(dir_name, exist_ok=True)
    print('下载了--->'+image_name)
    urlretrieve(image_url, dir_name+'/'+image_name)


### 从数据库查询数据
def getDatafromDataBase(conn,databaseName,sql):
    cur=conn.cursor()
    cur.execute('use '+databaseName)
    cur.execute(sql)
    persons=[]
    for i in cur.fetchall():
        persons.append(Person(i[0],i[1],i[2],i[3],i[4]))
    return persons


### 下载单个用户的图片
def getPersonImage(person):
    dir_name=person.id_number+person.name
    get_image(dir_name,person.id_front,dir_name+'front.jpg')
    get_image(dir_name,person.id_back,dir_name+'back.jpg')
    get_image(dir_name,person.driving_license,dir_name+'driving_license.jpg')


### 分批下载
def getPersonImageWithRange(start,end,persons):
    for i in range(start,end):
        print(i)
        try:
            getPersonImage(persons[i])
        except Exception as e:
            print(e)
            print(persons[i].name)


if __name__ == "__main__":
    conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='',charset='utf8')
    sql="SELECT name,id_number,id_front,id_back,driving_license FROM person dc where dc.id_front is not null;"
    p=getDatafromDataBase(conn,"person",sql)
    downloadThreads=[]
    print(len(p))
    for i in range(0,len(p),100):
        #print(i)
        downloadThread=threading.Thread(target=getPersonImageWithRange,args=(i,i+100,p))
        downloadThreads.append(downloadThread)
        downloadThread.start()
    for downloadThread in downloadThreads:
        downloadThread.join()
    print('Done')
