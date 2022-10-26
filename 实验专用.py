import requests
from bs4 import BeautifulSoup
import os
import time

# hd={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56"}

name1="20523"
url="https://bnman.net/comic/20523/1125495.html"
res=requests.get(url, timeout=(20,20))
soup=BeautifulSoup(res.text,'html.parser')

# print(res,soup,type(soup))
# lists=soup.find('ul',{"class":"jslist01"}).find_all('li')
scripts=soup.find_all('script')[8]
# for i in range(0,len(scripts)):
sre=str(scripts).split(';')
ll=sre[1].replace("var z_img='[","")

ll=ll.replace("]'","")
ll=ll.replace('"','')
ll=ll.strip()
lls=ll.split(",")
# urlss=urls.split(",")

print(lls)

# for i in range(1,len(lists)):
#     urls=lists[i].find('a').get('href')
#     chapter=lists[i].find('a').text
#     print(urls,chapter)