import requests
import json
from bs4 import BeautifulSoup as bfs
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
    with open('D://XinLangNewsHtml.txt','a') as f:
        f.write(json.dumps(content,ensure_ascii=False) + '\n')
  

def parse_one_page(html):
    pattern = re.compile('<h2>.*?href="(.*?)".*?blank">',re.S)
    items = re.findall(pattern,html)
    for item in items:
        print(item)
        write_to_file(item)
    
def get_page(num):
    url = "https://search.sina.com.cn/?c=news&q=%D2%BB%B4%F8%D2%BB%C2%B7&from=world&col=&range=all&source=&country=&size=&time=&a=&sort=rel&page="+str(num)
    k = "&pf=0&ps=0&dpc=1"
    url = url+k
    html = get_one_page(url)
    parse_one_page(html)
    

for i in range(50,100):
    get_page(i)


