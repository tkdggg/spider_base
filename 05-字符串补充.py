s = r"12\/345\/67iuy"
# s=s.split(']')

# print(s[-2:])
# def kill(str):
#     while (str.find('/') >= 0):
#         k=str.find('/')
#         str=str.replace(str[k], "+" ) # 正主为+
#         str=str.replace(str[k-1], "(" ) # 被杀者为（
#     str = str.replace("+", "/")
#     str = str.replace("(", '')
#     return str
# print(s.replace(s[3],'yfk'))
# s=kill(s)
# print(kill(s),type(s))
#


# s=({'12':121,'11':12112})
# print(s,type(s))
# 格式化输出
# a="dd, zz {}, laokei {}."
# a=a.format('yfk','wet pussy')
# print(a)


import requests
import os
from bs4 import BeautifulSoup




url='https://p_12.336t.com/sf_2/play/?list=https%3A%2F%2Fp_12.336t.com%2Fsf_2%2F20190310%2F3ae07f63e827fcc93d539afb4a01c0b6%2Fhls%2Fhls-480p.m3u8%3Fts%3D1642239084000%26token%3D9bb89929df2260e9305b0f12a729aad9&lpic=https%3A%2F%2Fp_12.336t.com%2Fsf_2%2F20190310%2F3ae07f63e827fcc93d539afb4a01c0b6%2Fthumb_800.jpg&pbppic=https%3A%2F%2Fp_12.336t.com%2Fsf_2%2F20190310%2F3ae07f63e827fcc93d539afb4a01c0b6%2Fpbp0.jpg&tlong=1686.92'



res=requests.get(url)
imgs=str(url)
sn=imgs[-9:]
# 设置一个变量，该变量为指定保存的路径,windows系统下的 D盘，test目录
dir_name = 'C:\\Users\\坦克迭戈\\Desktop\\cm1\\'

# 判断 D盘下是否存在 test目录，如果不存在该目录，则创建 test目录
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
# 在 D盘的 test目录下创建一个file.txt的文本，写入变量content
fb = open(dir_name+'.mp4',mode='wb')
fb.write(res.content)
print('创建完成...')
# file = open(sn,'wb')
# file.write(res.content)
# file.close()
print(res)
print(sn)












