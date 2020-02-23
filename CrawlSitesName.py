'''
@author: zhangwz
用于爬取陕西境内所有景点名称
'''
import re
import json
import urllib
import datetime
from urllib import request
import requests
import time
import os
import sys
import xlwt
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    #'Cookie': 'Hm_lvt_d1f759cd744b691c20c25f874cadc061=1538978413,1538984263; Hm_lpvt_d1f759cd744b691c20c25f874cadc061=1538997493; HAPPINESS_USER_LAST_SEARCH=%7B%22dep%22%3A%22PEK%22%2C%22arr%22%3A%22CAN%22%7D; Hm_lvt_4b7d84e5b348685ca608145cd1e1f6f0=1538984305; Hm_lpvt_4b7d84e5b348685ca608145cd1e1f6f0=1539144476',
    'Connection': 'keep-alive',
    'Cache-Control': 'no-cache'
}


#根据response返回数据，解析html获取相应的景点名称
def getSitesName():
    spotsNamesFile = 'shannxispotsData.txt'
    for i in range(47):
        #获取陕西景点名称的请求URL
        url = 'https://shannxi.cncn.com/jingdian/1-' + str(i + 1) + '-0-0.html'
        print(url)
        reponse = "" 
        result = "" #存放景点名称
        try:
            response = requests.get(url, headers=HEADERS, allow_redirects=False)
            if response.status_code == 200:
                html = response.content
                #print(html.decode("gbk"))
                try:
                    html = html.decode("gbk")
                    #return 'gbk'
                except:
                    pass
                #html = html.decode("gbk")
                #print(html)
                soup = BeautifulSoup(html, "html.parser")
                spots_list = soup.find('div', attrs={'class': 'city_spots_list'})
                #匹配景点名称节点
                names = spots_list.findAll('div', attrs={'class': 'title'})
                for name in names:
                    if name.find('b').string == '':
                        continue
                    spotName = name.find('b').string
                    #.strip()
                    print(spotName)
                    with open(spotsNamesFile, 'a', encoding='utf-8') as efw:
                        spotNameStr = '%s\n' % (spotName)
                        efw.write(spotNameStr)
        except requests.exceptions.ConnectionError:
            print("request failed")
    return spotsNamesFile
    
        #return url
if __name__ == "__main__":
    #开始运行时间
    starttime = datetime.datetime.now() 
    getSitesName()
    
    #结束运行时间
    endtime = datetime.datetime.now()
    #运行事假
    runAllTime = endtime - starttime
    #print(type(runAllTime))
    print("程序运行时长：" + str(runAllTime))
