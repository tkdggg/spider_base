import requests

url='https://passport.17k.com/login/'
hd={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55'
}

form_data={
    'loginName':'13168837959',
    'password':'a343105980',
}

# 构造请求，得到相应对象
login_res=requests.post(url,headers=hd,data=form_data)
print(login_res)
print(login_res.text)
# 获取登陆之后的头部信息（cookie）
headers=login_res.headers # 响应头部信息
get_cookie=headers['Set-Cookie']
cookie_split=get_cookie.split(';')
cookie=''
for i in cookie_split:

    if 'accessToken' in i:# 如果token在i里面，返回ture
        at=i.split(',')
        cookie=at[-1].strip()

print('最终得到的cookie：',cookie)










