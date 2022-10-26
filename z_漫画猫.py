import requests
from bs4 import BeautifulSoup
import os
import time
import lzstring

# let img_data_arr = LZString.decompressFromBase64(img_data).split(',');
string="JYWw5g9AbA7DCcECs8oGY0QOIFcB2eIA+gAwAcAtCdQHQBWADmADSiSwLKobb6GmVqARgBGNBnhZtocRCnSZcBYuSokATOMmtwMzvJ5L+q6urESpujnO6K+KwSTRbL7WVwW9lAtWnPbpaw9Dex9qABYXHTd9Wy9jR3D/Vz0bTyMHNSQowPcDO28TEiRk6NTggoS1KByrPLiMsJIoUtzY9NCimFqYtJDCxxhWuvb+quoyHvL8+MyJ4d6K2ab4KaCZxqL4BemGzsEhEjX6joGqQ531vbOSISFj0cq5u8uTsefNCzKr0/GhMwefSeYSEzi+bSByxMoNejyhB0i4JGkM2CNhKP252ySMWG0xtxKgKWqPONRxu1+zxaRLxNyE3XJP3eIKGNOuf0mjLewOhZHRxPxQlWXLhJNu2zZlLC6iOIoxNxl/Np43U9zlAoVoklzJM6k+AWRGpVAPVyrm6jBBtx7PNfm1PME6kRVopOsdSXt8Ko6mxLqZDu9hNNNulZL93K9GmpwaluoZ4dF+PUrJjbu9nIT8pVfM9YvUwszRvNEtTAacssLZrCaBISpDJjQasr9cEjbrsdb+pS/sjaBNzY7VAwufxGHbaaczu7EbFaA9pd7vuniZuaCDA4naDDy6zcy347LaHjO6L1ZTG8PGZPVYbOYXs4L15bQ5LF8j4QrT8HJA/B/fTa/Cdwi1e98XCLtvhnMD+0AstwktWD3ztUCbnCKdIJXcY0L/MVwiXDDdzCPCcLA7cCNPExwmjN9cOPcib0EcJz0Q3Cr3o58fzvGiwMfdjv3CV8WPxJBPz4icRJIm4kAAsSy2kyTxiQCCIQowQlIUuYkAQ2TIy0jSwiQdCVIYqhDP0kwkHw4yOMs8y1LI6zvyQaihKkujHPE5idLFJA2I8uSuNcxTeP83TBO8/EoFE0KxSiuyqCgGSYsikDuJuKBlMNEzmhgiL0u05L8vi5ojKyjioHnNLxigKyyu/GriqgBy6onJrGvclqy1gRq/M6yMoECvLqpCvrYvCwrxhgaLRvxKbipgJKZpuBb5sy61vxgXKJrmGACqWybkKqnbSvWicYEqoKdtq06yxgddLrCGBmpuyMnvmjqXrFOB5t6z7ZsG7bHpGv7lvG/a5jIaaQfGSHirIRboYh1KHpMMg1tdMs0bhvbEbCMhDpRwQyBOjHI2JuHrtJsUyHuoaIeeqn8TIFy6bxj7GZuMgvMB1Hfo5mGAfBvHgf5iGwdxkx4Ch0Wwil4r4ARmXJeR1nJfRnsxXgLahclnGlcEeACdVg2SY1/F4Au42qHgSmzZuG35YZu3xlQeX2eduZ4G5nWDb5j3ZcFiWDZF/3JfF/WKEOaXQ8oKP4sORWY8j25440EczkObWg+TvWk8OI2edjn906qQ5LcL5PbagjPilTp3q9L5pU/dhvMkOb3s8OP3W58LvU5DnvVEOcO88OEu24ucfe7uKeh5eWfY/+BfI/+ePQWXu4C59lfTcHxfy+3u4lyAA==="



txt=lzstring.LZString().decompressFromBase64(string).split(',')
url_len=len(txt)
print(txt)
print(url_len)
# hd={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56"}
for i in range(0,url_len):
    ti = str(time.time()) + '.png'
    url="https://mao.mhtupian.com/uploads/{}".format(txt[i])


    res = requests.get(url, timeout=(200, 200))
    while str(res)[-5:-2]!="200":
        res = requests.get(url, timeout=(200, 200))


    dir_name = 'C:\\Users\\坦克迭戈\\Desktop\\第七话\\'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    file = open(dir_name + ti, 'wb')  # ti  or  sn
    file.write(res.content)
    file.close()
    print(res)



# url="https://mao.mhtupian.com/uploads/img/6779/59631/Gunnm_06-001b.png"
# res=requests.get(url,timeout=(200,200))
# dir_name = 'C:\\Users\\坦克迭戈\\Desktop\\第七话\\'
# if not os.path.exists(dir_name):
#         os.mkdir(dir_name)
# file = open(dir_name + "06-001b.png", 'wb')  # ti  or  sn
# file.write(res.content)
# file.close()
# print(res,str(res)[-5:-2])
