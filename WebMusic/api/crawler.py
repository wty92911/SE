from pydoc import plain
import requests
import time
import json
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import pandas as pd





def read_cookie():
    Cookies = r"ntes_kaola_ad=1;__csrf=97edff3fb5469a0e96f88e5b85e0288a;MUSIC_U=b795617f9d6f56d32b4ce8b1926097d3f0e78835609bdde30d0a82a72f4aaf62993166e004087dd3a2e3b86a391ad7fe819c1113510e40a21d9b89283d11077825d3c7c7100e5e3dd4dbf082a8813684;__remember_me=true;YD00000558929251%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eed7e16a91f0a6bbe441b3b48fa7c54e878b8eacc449abee8397ea66f39fa1a5d72af0fea7c3b92a8cf18892f644b1b7ffd4cd6292a7b787d43fb88bacb5d343a1ae00d0cb54b2eb9ed1cf6abc94afaecc70ad939db8aa42f6e886b0f163b8bea7a9ca74a39a9ad4ef3bb3b6be86b364b5b39889b264ed9385a4f7348fadb999f35e97ae9794d867afa9a9d7c665929ba2b0d4458eb5fba4bc6af2f18eacb466818b8d8af566ab9caea5cc37e2a3;YD00000558929251%3AWM_NI=H%2FHqwHsi13NjRyyfQ5tUdTPIcr0%2FHXr5R0LbxLaMIdoMSW%2BJ68JOritbiHKxaFV3l1qjre0hwmXh3h%2FMKCt8MswxpVUrYsUmmwg6GoREnOQONk5C9b2%2FBK1nCUCivniDbDI%3D;_9755xjdesxxd_=32;__snaker__id=65Rv2cEyxzTdyCFg;WM_NI=A1esma0gr2VMm9tah%2B%2BEoAYLKjOKGJDWnRDpfKNIQu%2FWVs0cTLIdDrEzqn437Z%2FZ6xAL5AnuqtbKiblVZ2gI9ZezySJ9mKeAtE2jbqnEf98E5qkEc7Uu9ypNJMyAr1BGNHc%3D;WM_TID=abd17J%2FtVD1AFEAFEEbBSzjI7w3H6rpH;JSESSIONID-WYYY=EqYNG%2F7esQhyRz6%2BFmVnXfYgR1crs%2BggGd1DT3tSvDCqqtj062zoyd%2FAKJBhyOccvzC2x3ZeZM8xYiBi3bqe9hgZDrqU3RotcU3Z2okuu1SYYw%2BQ%2BXtl4bBZWsOS8w%2FCYk1%2F%2BbANYxhCh6KNlVxoxSw5sd9EWXBGRdl7hUDMjUR8C7j1%3A1663948436249;_ntes_nuid=9f09a56d4a7c5876eae6f1efcfad3171;WM_NIKE=9ca17ae2e6ffcda170e2e6ee90dc5092be8bb2b67481ac8aa3c84e839f9f86c144abb69697b3668a9a9ea4c22af0fea7c3b92a83efab94f06bf4b9bed3d547afe7bc82eb21e99ba1a2dc4889b681acc6428889a2b3c77ca69582aad47fed899a94b36998948785c77a87a6bf8fb739f586e1bbb5748394fba2ed7fb3acaeacec6ab08a96d3e643fb86ab9bfc598ae7a3ace84bb89bfe8be17bae9baadabb4ff7afa5a6e23d97abf79af3468a93b7a2f13b829982a9e237e2a3;WNMCID=fvshjo.1663946628693.01.0;WEVNSM=1.0.0;YD00000558929251%3AWM_TID=xbGLH%2FhfOeNEVUAQAQfAHj3Yu1i1B4CG;_ntes_nnid=9f09a56d4a7c5876eae6f1efcfad3171,1663946628491;NMTID=00O-ViZ9Dtz358euEN-oD7Q6bDWk-MAAAGDavKeYA;gdxidpyhxdE=B231AEUY%2FsSgY4ff8MBNH2XpEJykQKRfnnbC%5C13x%5CuyrI8PG7PyHSUzP%2BGedOBIql3OKzZggzvCj4uot9MxOYTRx7a3nKA5wqwdEol9pgy4V%5CoUPlxKco%5CSO%2FbxBsWDV6vOpG52TXI8sdIbm1%5CTgdcd3%2BnhS4sqDOgt4R%2Fu40%5CwJGgeI%3A1663947537608;_iuqxldmzr_=33"
    return Cookies

def get_cookies():
    driver = webdriver.Chrome()
    url = 'https://music.163.com/'
    driver.get(url)  # 发送请求
    # 打开之后，手动登录一次
    time.sleep(3)
    input('完成登陆后点击enter:')
    time.sleep(3)
    dictcookies = driver.get_cookies()  # 获取cookies
    cookie = [item["name"] + "=" + item["value"] for item in dictcookies]
    cookiestr = ';'.join(item for item in cookie)
    print(cookiestr)
    with open('wyycookie.txt', 'w') as f:
        f.write(cookiestr)
    print('cookies保存成功！')
    driver.close()

def get_headers():
    Cookies=read_cookie()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'Cookie': '{}'.format(Cookies)}
    return headers

rs = requests.session()


def get_newcomments(id):
    comments=[]
    url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_{}?limit=100&offset=1'.format(id)
    r = rs.get(url, headers=get_headers())
    r.encoding = 'utf-8'
    str_r = r.text
    dict_r = json.loads(str_r)
    print(dict_r['comments'][0])
    for i in range(100):
         comment=dict_r["comments"][i]['content']
         username = dict_r['comments'][i]['user']['nickname']
         comments.append((comment,username))
    return comments
def get_hotcomments(id):
    comments=[]
    url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_{}?limit=100&offset=0'.format(id)
    r = rs.get(url, headers=get_headers())
    r.encoding = 'utf-8'
    str_r = r.text
    dict_r = json.loads(str_r)
   # print(type(dict_r['hotComments']))
    #print(dict_r.keys())
    print(len(dict_r['hotComments']))
    for i in range(len(dict_r['hotComments'])):
        comment = dict_r["hotComments"][i]['content']
        username = dict_r['hotComments'][i]['user']['nickname']
        comments.append((comment,username))
    return comments

def get_ID(name):#返回五个搜索条目
    url = 'https://music.163.com/api/search/get/web?csrf_token=hlpretag=&hlposttag=&s={'+str(name)+'}&type=1&offset=0&total=true&limit=5'
    r = rs.get(url, headers=get_headers())
    r.encoding = 'utf-8'
    str_r=r.text
    dict_r = json.loads(str_r)
    #print(dict_r)
    #print(dict_r["result"]['songs'][0]['id'])
    ID=[dict_r["result"]['songs'][i]['id'] for i in range(0,5)]
    #print(dict_r["result"]['songs'][0]['artists'][0]['name'])
    return ID


def get_list(musiclistid):
        Info = []
        url = 'https://music.163.com/playlist?id={}'.format(musiclistid)
        rs = requests.session()
        r = rs.get(url, headers=get_headers())
        soup = BeautifulSoup(r.content, 'lxml')
        hide = soup.find('ul', {'class': 'f-hide'})
        a = hide.find_all('a')
        for every in a:
            data = []
            uid = re.search(r'id=(.*)', every['href'], re.M | re.I)
            uid = uid.group(1)
            data.append(uid)
            data.append(every.text)
            Info.append(data)
        # for i in Info:
        #     print(i[0])

        return Info

def get_lyric(id):
    url = 'https://music.163.com/api/song/lyric?id={}&lv=1&kv=1&tv=-1'.format(id)
    r = rs.get(url, headers=get_headers())
    r.encoding = 'utf-8'
    str_r = r.text
    dict_r = json.loads(str_r)
    return dict_r['lrc']['lyric']

def get_pic_url(id):
    url = "http://music.163.com/api/song/detail/?id={}&ids=%5B{}%5D".format(id,id)
    r = rs.get(url, headers=get_headers())
    r.encoding = 'utf-8'
    str_r = r.text
    dict_r = json.loads(str_r)
    pic_url = dict_r['songs'][0]['album']['picUrl']
    return pic_url
def get_Music_name(id):
    url = "http://music.163.com/api/song/detail/?id={}&ids=%5B{}%5D".format(id,id)
    r = rs.get(url, headers=get_headers())
    r.encoding = 'utf-8'
    str_r = r.text
    dict_r = json.loads(str_r)
    #print(dict_r['songs'][0])
    #artists_name =  dict_r['songs'][0]['album']['name']
    return dict_r['songs'][0]['name']
def get_artists_name(id):
    url = "http://music.163.com/api/song/detail/?id={}&ids=%5B{}%5D".format(id,id)
    r = rs.get(url, headers=get_headers())
    r.encoding = 'utf-8'
    str_r = r.text
    dict_r = json.loads(str_r)
    ##print(dict_r['songs'])
    artists_name =  [x['name'] for x in dict_r['songs'][0]['artists']]
    return artists_name
def get_Music_url(id):
    url = "http://music.163.com/api/song/enhance/player/url?id={}&ids=%5B{}%5D&br={}".format(id,id,999000)
    r = rs.get(url, headers=get_headers())
    r.encoding = 'utf-8'
    str_r = r.text
    dict_r = json.loads(str_r)
    player_url = dict_r['data'][0]['url']
    return player_url

def get_Hotlist():#return 4 id
    url = "http://music.163.com/discover/toplist?id=3778678"
    r = rs.get(url, headers=get_headers())
    r.encoding = 'utf-8'
    str_r = r.text
    pat3 = r'<li><a href="/song\?id=(\d*?)">.*?</a></li>'
    hot_song_id = re.compile(pat3).findall(r.text)
    return hot_song_id[0:8]
