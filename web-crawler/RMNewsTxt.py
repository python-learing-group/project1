# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 16:22:07 2019

@author: ASUS
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 20:11:13 2019

@author: ASUS
"""

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
    with open('D://RenMinNewsTxt.txt','a',encoding='utf-8') as f:
        f.write(content)
  

def parse_one_page(html):
    page=s.get(html).content
    soup=bfs(page,'lxml')
    data=soup.select('p')
    for i in data:
        if i.select('a')==[]:
            print(i.get_text())
            write_to_file(i.get_text())


for line in open("D://RenMinNewsHtml.txt"):
    parse_one_page(line)
    

