# bs4会把HTML源码各个标签节点转化成python对象
#
# from bs4 import BeautifulSoup
#
#
# import requests
# url="https://guoguo.hxt9881.com/manhua/diercibeiyishijiezhaohuan/"
# res=requests.get(url)
# soup=BeautifulSoup(res.text,'html.parser')
#
# lists=soup.find('ul',{'id':"chapter-list-1"}).find_all('li')
#
# for i in lists:
#     urls=i.find('a').get('href')
#     chapter=i.find('span',{'class':"list_con_zj"}).text
#     print(urls,type(urls))
#     print(chapter,type(chapter))



#简单使用一下
from xpinyin import Pinyin
p = "Tkllk"
# result = p.get_pinyin('小琳爱分享')
#此处结果：xiao-lin-ai-fen-xiang
p = Pinyin().get_pinyin(p,'')
#此处结果：xiaolinaifenxiang
# result = p.get_pinyin('小琳爱分享',' ')
#此处结果：xiao lin ai fen xiang
print(p,type(p)) #结果：xiao-lin-ai-fen-xiang











