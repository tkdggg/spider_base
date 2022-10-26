# post是一个需要提交表单数据的请求

import requests

# 定义请求连接
url='http://www.xinfadi.com.cn/getCat.html'

hd={
    'User-Agent': 't/537.36 (KHTML, liMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKike Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55'
}
# 定义提交的数据
from_data={
    'prodCatid':'1186'

}


res=requests.post(url,headers=hd,data=from_data)
print(res)

data=res.json()
data_list=data['list']
for i in data_list:
    # print(i)
    prodName=i['prodName']
    lowPrice=i['lowPrice']
    print(prodName,lowPrice)















