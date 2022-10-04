from pydoc import plain
import requests
import time
import json
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import pandas as pd





def read_cookie():
    try:

        print("[INFO]:正常尝试读取本地cookie")
        with open('wyycookie.txt', 'r', encoding='utf8') as f:
            Cookies = f.read()
            # print(Cookies)
    except:
        print("[ERROR]:读取失败，请手动登录并更新")
        get_cookies()
        with open('wyycookie.txt', 'r', encoding='utf8') as f:
            Cookies = f.read()
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

def get_ID(name):
    url = 'https://music.163.com/api/search/get/web?csrf_token=hlpretag=&hlposttag=&s={'+str(name)+'}&type=1&offset=0&total=true&limit=1'
    r = rs.get(url, headers=get_headers())
    r.encoding = 'utf-8'
    str_r=r.text
    dict_r = json.loads(str_r)
    #print(dict_r)
    #print(dict_r["result"]['songs'][0]['id'])
    ID=dict_r["result"]['songs'][0]['id']
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
def get_artists_name(id):
    url = "http://music.163.com/api/song/detail/?id={}&ids=%5B{}%5D".format(id,id)
    r = rs.get(url, headers=get_headers())
    r.encoding = 'utf-8'
    str_r = r.text
    dict_r = json.loads(str_r)
    #print(dict_r)
    artists_name =  dict_r['songs'][0]['album']['name']
    return artists_name
def get_Music_url(id):
    url = "http://music.163.com/api/song/enhance/player/url?id={}&ids=%5B{}%5D&br={}".format(id,id,999000)
    r = rs.get(url, headers=get_headers())
    r.encoding = 'utf-8'
    str_r = r.text
    dict_r = json.loads(str_r)
    player_url = dict_r['data'][0:5]['url']
    return player_url

   
