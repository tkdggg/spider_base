# 爬虫
# 爬虫分类：通用式，聚焦式，增量式
# 爬虫原理：请求和响应
#url链接的组成部分
#
# coolie
# 保存在客户端的身份信息，密码什么的
# session,用户身份令牌
# import phone
#
# t="19161020027"
#
# l=t.Phone()
#
# print(l)

import requests as re

url='https://game.gtimg.cn/images/lol/act/img/skin/big1000.jpg'
hd = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
}
r=re.get(url,headers=hd)
print(r)
# file=open('big1000.jpg',r)













