# -*- coding: utf-8 -*-

import requests
import json
import re
import time
from bs4 import BeautifulSoup as bfs
new_urls=[]
global s
s = requests.session()

def get_one_page(url):
    try:
        kv = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
        r = requests.get(url,headers = kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("爬取失败")
        
def write_to_file(content):  
    with open('D://RenMinNewsTxt3.txt','a') as f:
        f.write(json.dumps(content,ensure_ascii=False) + '\n')
  

def parse_one_page(html):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
        'Upgrade-Insecure-Requests': '1',
        'Referer': 'http://search.people.com.cn/cnpeople/news/getNewsResult.jsp',
        'Host': 'search.people.com.cn',
        'Origin': 'http://search.people.com.cn',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'max-age=0'
    }

    requests.adapters.DEFAULT_RETRIES = 5
    s.keep_alive = False
    page=s.get(html).content
    soup=bfs(page,'lxml')
    data=soup.select('p')
    head=soup.select('h1')
    #print(head.get_text())
    #write_to_file(head.get_text())
    for i in data:
        if i.select('a')==[]:
            print(i.get_text())
            #write_to_file(i.get_text())

def get_page(num,key):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
        'Upgrade-Insecure-Requests': '1',
        'Referer': 'http://search.people.com.cn/cnpeople/news/getNewsResult.jsp',
        'Host': 'search.people.com.cn',
        'Origin': 'http://search.people.com.cn',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'max-age=0'
        }
    url = 'http://search.people.com.cn/cnpeople/news/getNewsResult.jsp'####获得页面的端口
    posturl = 'http://search.people.com.cn/cnpeople/search.do'###提交数据的服务端口
    formdata = {'siteName': 'news',
                'pageNum': str(num),
                'keyword': key.encode('gbk'),
                'facetFlag': 'null',
                'nodeType': 'belongsId',
                'nodeId': '0',
                'pageCode': '',
                'originName': ''}
    s.post(posturl, data=formdata, headers=headers,timeout=5)#提交请求数据
    time.sleep(0.2)
    page = s.get(url, headers=headers,timeout=10)#获得请求的页面
    html=page.content
    soup=bfs(html,'lxml')#解析页面
    urls=soup.select('ul li b a[href]')#选择值
    # print(html.decode('gbk'))
    f=open('D://RenMinNewsHtml.txt','a+')
    for i in urls:
        new_urls.append(i['href'])
        # html = get_one_page(i['href'])!!!!!!!!!!!!!!!!!!!!!!!!!这是一个访问，严禁不加time.slepp()直接放在for循环
        print(num,i['href'])
        f.write(i['href']+ '\n')
    f.close()
   

for i in range(50,90):
    try:
      get_page(i,'一带一路')
      time.sleep(1)
    except:
      print(str(i)+'页 错误')

    




