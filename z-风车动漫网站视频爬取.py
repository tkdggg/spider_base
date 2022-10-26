import requests
from bs4 import BeautifulSoup
import os
import time
from xpinyin import Pinyin

# 提取图片链接
def kill(str):
    while (str.find('/') >= 0):
        k=str.find('/')
        str=str.replace(str[k], "+" ) # 正主为+
        str=str.replace(str[k-1], "(" ) # 被杀者为（
    str = str.replace("+", "/")
    str = str.replace("(", '')
    return str

# 下载章节内漫画
def download(imgs,na,name):
    url=imgs
    res = requests.get(url,timeout=(20,20))
    ti=str(time.time())+'.jpg'
    # sn = imgs[-9:]    #以图片末尾命名
    dir_name = 'C:\\Users\\坦克迭戈\\Desktop\\{}\\{}\\'.format(name,na)
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    file = open(dir_name + ti, 'wb')# ti  or  sn
    file.write(res.content)
    file.close()
    print(res)
    print(sn)

# 获得章节HTML
def chapters(urls,chapter,name):
    url='https://guoguo.hxt9881.com{}'.format(urls)

    #提取图片链接
    res=requests.get(url,timeout=(20,20))
    html_text=res.text
    soup=BeautifulSoup(html_text,'html.parser')
    script=soup.find_all('script')[3].text
    script=script.replace(';var chapterImages = [','')
    script=script.split(']')
    imgs=script[0].replace('"','')
    imgs=kill(imgs)
    imgs=imgs.split(',')

    # print(imgs[3],type(imgs))
    for i in imgs:
        download(i,chapter,name)
    print('finish  !')


# 获得目标漫画链接
name=input("请你输入目标漫画：")
dir_name = 'C:\\Users\\坦克迭戈\\Desktop\\{}\\'.format(name)      #创建漫画文件夹
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

name1= Pinyin().get_pinyin(name,'')
url="https://guoguo.hxt9881.com/manhua/{}/".format(name1)
res=requests.get(url,timeout=(20,20))
soup=BeautifulSoup(res.text,'html.parser')
lists=soup.find('ul',{'id':"chapter-list-1"}).find_all('li')
for i in lists:
    urls=i.find('a').get('href')
    chapter=i.find('span',{'class':"list_con_zj"}).text
    chapter=chapter.replace(' ','')
    chapters(urls,chapter,name)
    # print(urls,type(urls))
    # print(chapter,type(chapter))















