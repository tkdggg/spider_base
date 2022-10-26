import requests

hd= {
    "user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55'
    }

def get_hero_skins(ids):
    url="https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js?ts=2735907".format(ids)

    res=requests.get(url,headers=hd)
    # print(res.text)

    data=res.json()
    print(type(data),data)

    # print(data.keys())
    skins = data['skins']

    for sk in skins:
        mainImg = sk['mainImg'] #皮肤链接
        name=sk['name']
        if mainImg:
            print(sk)
            img_res = requests.get(mainImg,headers=hd)
            sn="./img/"+name+".jpg"
            file = open(sn,'wb')
            file.write(img_res.content)
            file.close()


hero_list_url = "https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?v=04"
res = requests.get(hero_list_url,headers=hd)
data = res.json()
hero_list = data['hero']e/4b60005d46ed88fd4b22a1c0b759.jpg
# https://n2a.qwzhe.com/images/p/de/a
for hero in hero_list:
    print(hero)
    heroId = hero['heroId']
    # print(heroId)
    # get_hero_skins(heroId)   #下载皮肤


# https://n2a.otzyx.com/images/p/9d/b7/03fee77075ebd53d8d49151bcf59.jpg
# https://n2a.hapilai.cn/images/p/38/98/be25c1f2c46c3d157dc464db63f9.jpg















