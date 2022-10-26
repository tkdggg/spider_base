import requests
from bs4 import BeautifulSoup
import os
import time

def download(imgs,name,chapter):
    url = "https://img.hngxgt.net/{}".format(imgs)
    res = requests.get(url, timeout=(20, 20))
    print(res)
    ti = str(time.time()) + '.jpg'
    dir_name = 'C:\\Users\\坦克迭戈\\Desktop\\{}\\{}\\'.format(name, chapter)
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    file = open(dir_name + ti, 'wb')  # ti  or  sn
    file.write(res.content)
    file.close()
    print(res)

# 获取详细页面漫画链接
def chapters(urls,chapter,name):
    url="https://bnman.net{}".format(urls)
    res=requests.get(url,timeout=(20,20))
    soup = BeautifulSoup(res.text, 'html.parser')
    print(res)
    # 提取漫画每页链接
    scripts = soup.find_all('script')[8]
    sre = str(scripts).split(';')
    ll = sre[1].replace("var z_img='[", "")
    ll = ll.replace("]'", "")
    ll = ll.replace('"', '')
    ll = ll.strip()
    lls = ll.split(",")
    for i in lls:
        download(i,name,chapter)
    print("flish!!!")

name=input("请你输入目标漫画：")
dir_name = 'C:\\Users\\坦克迭戈\\Desktop\\{}\\'.format(name)      #创建漫画文件夹
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
# 获取漫画章节 链接
name1="3092"
url="https://bnman.net/comic/{}.html".format(name1)
res=requests.get(url,timeout=(20,20))
print(res)
soup=BeautifulSoup(res.text,'html.parser')
lists=soup.find('ul',{'class':"jslist01"}).find_all('li')

for i in range(1,len(lists)):
    urls=lists[i].find('a').get('href')
    chapter=lists[i].find('a').text
    chapters(urls,chapter,name)
    # print(urls,chapter)