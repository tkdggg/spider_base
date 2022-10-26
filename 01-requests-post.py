"""
post请求
    需要提交表单数据的请求
"""

import requests
import csv
#创建文件编辑对象
file = open('蔬菜价格大全.csv', 'w', encoding='utf-8-sig', newline='')
#创建csv的编辑对象
file_csv = csv.writer(file)
file_csv.writerow( ['菜品名称','最低价','最高价','平均价','产地','单位','发布时间'] )


#定义请求的链接
url = "http://www.xinfadi.com.cn/getPriceData.html"
#定义请求头部信息
hd = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'
}
# 定义提交的数据
from_data = {
    'limit': '20',
    'current': '4',
    'pubDateStartTime': '',
    'pubDateEndTime': '',
    'prodPcatid': '',
    'prodCatid': '',
    'prodName': '',
}
#构造请求，得到响应的对象
res = requests.post(url, headers=hd, data=from_data)
print(res)
print( res.text)
data = res.json()
data_list = data['list']
for i in data_list:
    prodName = i['prodName'] # 菜品名称
    lowPrice = i['lowPrice'] # 最低价
    highPrice = i['highPrice'] # 最高价
    avgPrice = i['avgPrice'] # 均价
    place = i['place'] # 产地
    unitInfo = i['unitInfo'] # 单位
    pubDate = i['pubDate'] # 发布日期
    writerows = [prodName,lowPrice,highPrice,avgPrice,place,unitInfo,pubDate]
    file_csv.writerow( writerows   )