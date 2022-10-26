
"""
1、通过代码进行登录请求
2、登录成功之后获取token身份令牌
3、访问请求书架信息，需要携带token身份令牌

"""

import requests

#登录的请求链接
login_url = "https://passport.17k.com/ck/user/login"
#请求头部的信息
login_hd = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
# 指定post请求参数
form_data = {
    'loginName': '13168837959',
    'password': 'a343105980',
}
#构造请求, 得到响应对象
login_res = requests.post(login_url, headers=login_hd, data=form_data)
# print(login_res)
# print(login_res.text)
# 获取登录之后的头部信息（cookie）
headers = login_res.headers # 响应的头部信息
get_cookie = headers['Set-Cookie']
cookie_split = get_cookie.split(';')
cookie = "" # 用作 最终获取的cookie值
for i in cookie_split:
    if 'accessToken' in i:# 如果token再i里面，会返回True
        at = i.split(',')
        # 字符串.strip()   默认去除首尾的空格 空字符 换行..
        cookie = at[-1].strip()



print('最终得到的cookie是：', cookie)

#请求书架的接口链接
books_url = "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"
# 请求头部信息
hd = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
    'cookie' : cookie
}
# 构造请求得到响应对象
book_res = requests.get(books_url, headers=hd)
print(book_res)
print(book_res.text)
