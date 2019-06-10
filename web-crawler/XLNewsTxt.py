# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 08:09:23 2019

@author: ASUS
"""

import requests
import json
import re
import time
from bs4 import BeautifulSoup as bfs


def write_to_file(content):  
    with open('D://XinLangNewsTxt.txt','a',encoding='utf-8') as f:
        f.write(content+'\n')
        
def parse_one_page(html):
    s = requests.session()
    page = s.get(html).content
    soup=bfs(page,'lxml')
    data=soup.select('p')
    for i in data:
        if i.select('a')==[]:
            print(i.get_text())
            write_to_file(i.get_text())
    
for line in open("D:\\XinLangNewsHtml.txt"):
    parse_one_page(line)
    