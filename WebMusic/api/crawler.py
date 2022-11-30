from pydoc import plain
import requests
import time
import json
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import pandas as pd
import time




def read_cookie():
    Cookies = r"ntes_kaola_ad=1;__csrf=97edff3fb5469a0e96f88e5b85e0288a;MUSIC_U=b795617f9d6f56d32b4ce8b1926097d3f0e78835609bdde30d0a82a72f4aaf62993166e004087dd3a2e3b86a391ad7fe819c1113510e40a21d9b89283d11077825d3c7c7100e5e3dd4dbf082a8813684;__remember_me=true;YD00000558929251%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eed7e16a91f0a6bbe441b3b48fa7c54e878b8eacc449abee8397ea66f39fa1a5d72af0fea7c3b92a8cf18892f644b1b7ffd4cd6292a7b787d43fb88bacb5d343a1ae00d0cb54b2eb9ed1cf6abc94afaecc70ad939db8aa42f6e886b0f163b8bea7a9ca74a39a9ad4ef3bb3b6be86b364b5b39889b264ed9385a4f7348fadb999f35e97ae9794d867afa9a9d7c665929ba2b0d4458eb5fba4bc6af2f18eacb466818b8d8af566ab9caea5cc37e2a3;YD00000558929251%3AWM_NI=H%2FHqwHsi13NjRyyfQ5tUdTPIcr0%2FHXr5R0LbxLaMIdoMSW%2BJ68JOritbiHKxaFV3l1qjre0hwmXh3h%2FMKCt8MswxpVUrYsUmmwg6GoREnOQONk5C9b2%2FBK1nCUCivniDbDI%3D;_9755xjdesxxd_=32;__snaker__id=65Rv2cEyxzTdyCFg;WM_NI=A1esma0gr2VMm9tah%2B%2BEoAYLKjOKGJDWnRDpfKNIQu%2FWVs0cTLIdDrEzqn437Z%2FZ6xAL5AnuqtbKiblVZ2gI9ZezySJ9mKeAtE2jbqnEf98E5qkEc7Uu9ypNJMyAr1BGNHc%3D;WM_TID=abd17J%2FtVD1AFEAFEEbBSzjI7w3H6rpH;JSESSIONID-WYYY=EqYNG%2F7esQhyRz6%2BFmVnXfYgR1crs%2BggGd1DT3tSvDCqqtj062zoyd%2FAKJBhyOccvzC2x3ZeZM8xYiBi3bqe9hgZDrqU3RotcU3Z2okuu1SYYw%2BQ%2BXtl4bBZWsOS8w%2FCYk1%2F%2BbANYxhCh6KNlVxoxSw5sd9EWXBGRdl7hUDMjUR8C7j1%3A1663948436249;_ntes_nuid=9f09a56d4a7c5876eae6f1efcfad3171;WM_NIKE=9ca17ae2e6ffcda170e2e6ee90dc5092be8bb2b67481ac8aa3c84e839f9f86c144abb69697b3668a9a9ea4c22af0fea7c3b92a83efab94f06bf4b9bed3d547afe7bc82eb21e99ba1a2dc4889b681acc6428889a2b3c77ca69582aad47fed899a94b36998948785c77a87a6bf8fb739f586e1bbb5748394fba2ed7fb3acaeacec6ab08a96d3e643fb86ab9bfc598ae7a3ace84bb89bfe8be17bae9baadabb4ff7afa5a6e23d97abf79af3468a93b7a2f13b829982a9e237e2a3;WNMCID=fvshjo.1663946628693.01.0;WEVNSM=1.0.0;YD00000558929251%3AWM_TID=xbGLH%2FhfOeNEVUAQAQfAHj3Yu1i1B4CG;_ntes_nnid=9f09a56d4a7c5876eae6f1efcfad3171,1663946628491;NMTID=00O-ViZ9Dtz358euEN-oD7Q6bDWk-MAAAGDavKeYA;gdxidpyhxdE=B231AEUY%2FsSgY4ff8MBNH2XpEJykQKRfnnbC%5C13x%5CuyrI8PG7PyHSUzP%2BGedOBIql3OKzZggzvCj4uot9MxOYTRx7a3nKA5wqwdEol9pgy4V%5CoUPlxKco%5CSO%2FbxBsWDV6vOpG52TXI8sdIbm1%5CTgdcd3%2BnhS4sqDOgt4R%2Fu40%5CwJGgeI%3A1663947537608;_iuqxldmzr_=33"
    #Cookies = r'MUSIC_R_T=1552132782219; MUSIC_A_T=1552132341427; _ntes_nnid=4a084381513cfe30158ffc5f52358e03,1663376872871; _ntes_nuid=4a084381513cfe30158ffc5f52358e03; NMTID=00O3B60ow3vdvuWIE4dp0tN61gFu00AAAGDSPzWdA; WEVNSM=1.0.0; WNMCID=poyqys.1663376872979.01.0; WM_TID=j8QI0YwkMDVBRBQQBAPEC3HUrvTykTDU; WM_NI=22fJFO3OHZ05/Sl1QdFSvX94BiLyt9G4+nJYf6numlBoqiId6HqVdxKYMuPVSVpL2tQprhvScSp5trSSP0c1de1DxzHARI5LxCEVIaQ+G7w2z/2AgMhNAMa5d9gcA6URWHE=; WM_NIKE=9ca17ae2e6ffcda170e2e6eed2e754abbcfad9d96b8b9e8fb3d54e928e9ab0d84682eeb7babb62fcec8aa2f72af0fea7c3b92af2eeaaabc545f19188bbb33fed8da4d2d470868dbab9bc4082b7849af73385ece58fc953a6eaa296f06882b1bf8acc70f698bfb7e77489878396d35e918ac0adb18093b0be89f559a18dc0d6f77a918da0d1e23ba8bbffa5fb728c9f9eaab848bc9d8bb7cc6b93f589d8f63abaf1fea2e647ac928faee43fa8e7a984c43e978e99a9c837e2a3; JSESSIONID-WYYY=am5YCMClx0OMKdpydlbYPI1DD/a08+2eA8My5PuEGtQeiiy8F8JkCh3wuNmZnYMmt482QzRlcV+76beuyVmOKdqTetQat2UuTTe\qOSdHWhKqgJusNUd3DQOjJzDZqyo4UYMvBPeSj\juYbmnzKKyj8g8vfh2jrfBpPzv\6vBEouvAev:1667210044636; _iuqxldmzr_=33; __snaker__id=2NDYVa84Ul2HoNfH; gdxidpyhxdE=H5NjGXoauSHs4TLS1dTAdjKI6HUAC/\1+Wx9DbvQQQI5bnoQfMYtKsftKU9RfjCsND9q7oOi1AZeZ4VfmQsGDXxW5lHUX\w5Ti8lGg185/hIHan8xvvKV9HnjPme5rYzCT1pWmAzgT1jlDkQsESvj7XLrdzS/mVmtBto91TyLqKwlb4x:1667209145229; YD00000558929251:WM_NI=aMAgbCOOLtu7Tgk9hs3r8ReKyznnl63am2Bc+0d/OmtdDRTqYSR9syGjpUTdS3xnY2tUZVe7/yokDJ1e/SsUSIaq6+ZduQ7IsAzG5c7KyFus6u5w2Twsu4Fy8dMXP+blbWU=; YD00000558929251:WM_NIKE=9ca17ae2e6ffcda170e2e6eeaedc4088f5ffbbd8439bb08ea2c85b979e8b82d14787b2b6bbb863f68e96d7db2af0fea7c3b92aa3938f88e1498d918495f83d98b9a5daeb79f1aef8b3e841bba6a28fef3ef1bfa3d3c169e9f0acd0ce67b8bc8cb3d77b9b8d9edaf27385b6c0b6d77091edb88fdc3ab88b96b7e83deda7a18cc742f3bbe1b4f25f9197af92b5219abcbbb2b643b19fb6a8b869f595b7a7f879f6abfb98b160b5adbbd5c573fcbc83b9d321a2b4aeb8d837e2a3; YD00000558929251:WM_TID=faxLl+u6vkJAUFUQVVfUYAiiZpn/EdrT; __csrf=00a694732c90be03994eaff0ce06f32d; MUSIC_U=d6df74e432afd28fc1a02fe6ba98417479cdeeff8966da01d21f6ba19445c54d1e8907c67206e1edec8ca36c6eeee7365403727f7bf792c6d68434e00a803293662ac4f026c2e1e1d4dbf082a8813684; ntes_kaola_ad=1'
    #Cookies = r'MUSIC_A_T=1548313965570; MUSIC_R_T=1548315334656; _ntes_nnid=4a084381513cfe30158ffc5f52358e03,1663376872871; _ntes_nuid=4a084381513cfe30158ffc5f52358e03; NMTID=00O3B60ow3vdvuWIE4dp0tN61gFu00AAAGDSPzWdA; WEVNSM=1.0.0; WNMCID=poyqys.1663376872979.01.0; WM_TID=j8QI0YwkMDVBRBQQBAPEC3HUrvTykTDU; __snaker__id=2NDYVa84Ul2HoNfH; YD00000558929251:WM_TID=faxLl+u6vkJAUFUQVVfUYAiiZpn/EdrT; ntes_kaola_ad=1; WM_NI=+BBvBiILdq8LV51qLzlTBIWE6mBdQxOMmLdh9Dgj982obEVGIWEkOUGS8q6lOfhhUXIdYN71vR2MkAuoYvx3qn863LG3pZDSATx3WALsUiUSehtfq8X/OQFYd/ptqKcfSk0=; WM_NIKE=9ca17ae2e6ffcda170e2e6ee8df853879cfbb0b34d918e8ab6c54a939f8a87d47096aa8d84d343b08aa6b0d32af0fea7c3b92ae99e8e97c1638b94ac92bb4896ebff92cf72b08c8eaad64ff6b38e85d4748d93a3ade764fb9ca98bbc34f2b1aea6d54d8b898b8cce5f858df892b5688dbaa889d8548bbc97afb63bb68efeaeea4bb7b19797fb39b3b2f8d7b24885edc0bbc759838cb8d4d64b90ad9b8ad859a7b8bc87f4349cf181b2c553a8f1c095f441a1ba9d8cb337e2a3; JSESSIONID-WYYY=grnOvPn0dFq1/EMaIQw3xmyHxy3vzd0CE4Vv7Vlutb5PPABlvez6R2cf/DAkR3eDc1Xxg0h0HGZxD3fi0F0z7tZPeqwpR/2pSTkaOlqrBsX2sluE1Ml2pmYfVxZa4M8jfK3v/5C4SRwE44rFmkcM4FRDnXiWlsz+dHJg/quOIE90N1cq:1667410482315; _iuqxldmzr_=33; gdxidpyhxdE=GZ+8Qn0i3LC3c4DEjDsBGgCb8EHVfZiKsT7hGhnO33vtidMtGpOwi6qp5JcNJNwbs1JP8hWm2M8jccj2ZoyQ5y5AwXzXEEDeaKchXjuPSN9E6qD8nCwNsxDuVSbgXD6fPinY7DwpXU0+a/yaBd/jKgotXRxNVJjIBeJ7dJqb0QTgfhyG:1667409582546; YD00000558929251:WM_NI=77DO2Fr/BulRVzpnGK6mwEQP1NxwLd7vkyk5kMP9JTNQ3AmZfIibKZNjDOFgprIj4D9zDR/wYri/YIlnIIU8KzKQsmhKBZrmNFB3AVsFbcybvWrFBBPIDPsRPJyVEJhoVnk=; YD00000558929251:WM_NIKE=9ca17ae2e6ffcda170e2e6eebafc7ff6bfa0d4b85398b08ba3c45e879e9e87d54386ae99aad343abafa584c42af0fea7c3b92af5e98cb0b14eb2f18e96ef5a96a6c08fc641f6b3b9a6d45cf392b898cf70f5aaa59aea3fa993a0dac9608e8ffda2f052a697a783ca528eb68cb0c56db4ae878bb750fba68cb3ae7d9baea7d0dc43b0b287aad83489a685b2f267ac958ebbf1678e9a8ed4c45eb19aae84fc6ab689bea7c14a94978cb1f25a9496b7b7c842acb19a8fea37e2a3; __csrf=67d8c09d2ba4385009b505986ad637e9; __remember_me=true; MUSIC_U=b795617f9d6f56d32b4ce8b1926097d3f3f77da6fe519dbf27f769a1e836e299993166e004087dd3b9cbdfe5aaa8f091ebd0279d6cfa394a1d9b89283d11077825d3c7c7100e5e3dd4dbf082a8813684'
    #Cookies = r'MUSIC_R_T=1548315334656; MUSIC_A_T=1548313965570; _ntes_nnid=da6c954e4f752a2b920124b33e18c452,1667409090230; _ntes_nuid=da6c954e4f752a2b920124b33e18c452; NMTID=00Oh2JeIuN0SOv_LkM8rl_Yw9edwX8AAAGEOVOXUw; WEVNSM=1.0.0; WNMCID=mfjvni.1667409090344.01.0; WM_NI=T3ivkkg5mCyai+LlpJLlGhEJcPjW+o2JMR6SwBSDXReYD9BGH1a5M5UsvJkHnh67RwhNYav89hWeMUfFHGcmR0DXoZYUT0LK7+tAQOmrxfprW0zDKnvemysv22L+AwweNHg=; WM_NIKE=9ca17ae2e6ffcda170e2e6ee87db7d8a8988adc854b2868aa2d14b838e9f83c54783ab8daaef7e88efaeb6c62af0fea7c3b92a98eda797ea61a5eba3a4fc6babf5848df34290b48989c842a190a6b8aa65f29683b3b559b59e9da5db5aa7878cdac14d8cefafd6d03f97adbaabea44aeb8fad8d17dac929782f534fbb89986d05fa69a88a8e26792f08cb9ee529b8b9cd1cf41f5f5bca2d445afaeb887f37a95f0b6a5ca66b6bba39af27ef2ee84ccc47db5bb82a9e637e2a3; WM_TID=Rpk+kTBWqm9AUFERUALQME+WJxuSgeBT; JSESSIONID-WYYY=m0hEhZ1up4W6e9ne4878m+Wu+Ti6Y//2W68FrelPQdJiWgcA480rUHtimtoRcPnp4oavho1uDXZBErMWbuvlhnWh3QHXCicGKkHN0QmGOVUl2p5u1dF97IK8IXrNJvn9DSUyxUdJq4exx7PmhP7nJJQlbfYfSqb0pAVvNv1hRb9m\XNQ:1667410892462; _iuqxldmzr_=33; __snaker__id=DCSf6ddz8DNJA1kg; gdxidpyhxdE=2TGLci6cCzidxL9NTQiOQE8CwosjvOV3L4UNli10g1ODPjPwooNrXTVv580mxVBX/wWq7RtwbUZGRPcwftyayOyCUPthNYukOt3NwPwKYVROMx3qEgNVdElBY3lCjQSMJCOeWNRQts86koBw1XrQIeEZB6a3Y7Zmzw9+KaRD6PhUUfjZ:1667409992683; YD00000558929251:WM_NI=1Qm0s3Vd4D9PTh8nH3fNXW2pQN0dWw3+y2Y21T57izg7e8ldO4FpFOhQ8CiVS73VWoXQcBODyZm4CAOVs4bGJap0aAhyKM/bc8odtYj8cNUFa1gAO16PABrOkTwq6pVra1A=; YD00000558929251:WM_NIKE=9ca17ae2e6ffcda170e2e6ee95f369e9b7fba9cb80fbeb8ba7d45f828e9b82c54396ea8dabeb3da19ea69ad82af0fea7c3b92af38fa3d1f23996bcfca5bc5c98b8f88fcb39a69298b8b17c93920085d67df1f5b7d3dc3af38cfbd8ec72a5e9abd9ef708dec8a91c545ac8ff8a4ec5e91e9fdb7d6659c8fada3ce50bb86a3d5c24b8d8abdd5e14d8abfc0d1e44baca785aeae6aa1e8a185f753aae8adafd84ea3efa9a2ce3bf6908fa3f145a98cb992b57c96aeafd2c437e2a3; YD00000558929251:WM_TID=r4twiA/cVTpFRFFARRbBNF+DZl6dEz3E; MUSIC_U=b795617f9d6f56d32b4ce8b1926097d3f3f77da6fe519dbf6f4d5aeeb04e6f16993166e004087dd39f78822fd9653ecd37d02f30ab79cc461d9b89283d11077825d3c7c7100e5e3dd4dbf082a8813684; __csrf=f10ef8b27cbc6902409dae05eedab5aa; __remember_me=true; ntes_kaola_ad=1',
    Cookies = r'MUSIC_A_T=1667410108592; MUSIC_R_T=1667410155490; _ntes_nnid=da6c954e4f752a2b920124b33e18c452,1667409090230; _ntes_nuid=da6c954e4f752a2b920124b33e18c452; NMTID=00Oh2JeIuN0SOv_LkM8rl_Yw9edwX8AAAGEOVOXUw; WEVNSM=1.0.0; WNMCID=mfjvni.1667409090344.01.0; WM_NI=T3ivkkg5mCyai+LlpJLlGhEJcPjW+o2JMR6SwBSDXReYD9BGH1a5M5UsvJkHnh67RwhNYav89hWeMUfFHGcmR0DXoZYUT0LK7+tAQOmrxfprW0zDKnvemysv22L+AwweNHg=; WM_NIKE=9ca17ae2e6ffcda170e2e6ee87db7d8a8988adc854b2868aa2d14b838e9f83c54783ab8daaef7e88efaeb6c62af0fea7c3b92a98eda797ea61a5eba3a4fc6babf5848df34290b48989c842a190a6b8aa65f29683b3b559b59e9da5db5aa7878cdac14d8cefafd6d03f97adbaabea44aeb8fad8d17dac929782f534fbb89986d05fa69a88a8e26792f08cb9ee529b8b9cd1cf41f5f5bca2d445afaeb887f37a95f0b6a5ca66b6bba39af27ef2ee84ccc47db5bb82a9e637e2a3; WM_TID=Rpk+kTBWqm9AUFERUALQME+WJxuSgeBT; JSESSIONID-WYYY=m0hEhZ1up4W6e9ne4878m+Wu+Ti6Y//2W68FrelPQdJiWgcA480rUHtimtoRcPnp4oavho1uDXZBErMWbuvlhnWh3QHXCicGKkHN0QmGOVUl2p5u1dF97IK8IXrNJvn9DSUyxUdJq4exx7PmhP7nJJQlbfYfSqb0pAVvNv1hRb9m\XNQ:1667410892462; _iuqxldmzr_=33; __snaker__id=DCSf6ddz8DNJA1kg; YD00000558929251:WM_NI=1Qm0s3Vd4D9PTh8nH3fNXW2pQN0dWw3+y2Y21T57izg7e8ldO4FpFOhQ8CiVS73VWoXQcBODyZm4CAOVs4bGJap0aAhyKM/bc8odtYj8cNUFa1gAO16PABrOkTwq6pVra1A=; YD00000558929251:WM_NIKE=9ca17ae2e6ffcda170e2e6ee95f369e9b7fba9cb80fbeb8ba7d45f828e9b82c54396ea8dabeb3da19ea69ad82af0fea7c3b92af38fa3d1f23996bcfca5bc5c98b8f88fcb39a69298b8b17c93920085d67df1f5b7d3dc3af38cfbd8ec72a5e9abd9ef708dec8a91c545ac8ff8a4ec5e91e9fdb7d6659c8fada3ce50bb86a3d5c24b8d8abdd5e14d8abfc0d1e44baca785aeae6aa1e8a185f753aae8adafd84ea3efa9a2ce3bf6908fa3f145a98cb992b57c96aeafd2c437e2a3; YD00000558929251:WM_TID=r4twiA/cVTpFRFFARRbBNF+DZl6dEz3E; ntes_kaola_ad=1; gdxidpyhxdE=uZii2acdOJUJ59hh3xysgH53dg5NR96YD2\VXopPsVzZ9c1Stx2csdh0lTeIp1fBVZ+mLfJBlb5Hd25SVPnjUJ4APwCnRTNyH98yLuo3bauVwHyz4t5NKrjZ7V3joBl\MZCwh4pzV4BdLqfmc6e8ACec04C0l2LZjhpExmD\/+bcRUr8:1667410832655; MUSIC_U=824dd9c94723b4edd71aab77239f7d24f3f77da6fe519dbf64568088c5411417993166e004087dd3a96a6fe47183b1266ec91e70450ec46a3a1707d7d2c93fc174f55d6a98f2f57dd4dbf082a8813684; __remember_me=true; __csrf=a003e1ca1f5902895bc9fbf644f13992'
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

def get_ID(name):#返回至多18个搜索条目
    url = 'https://music.163.com/api/search/get/web?csrf_token=hlpretag=&hlposttag=&s={'+str(name)+'}&type=1&offset=0&total=true&limit=18'
    r = rs.get(url, headers=get_headers())
    r.encoding = 'utf-8'
    str_r=r.text
    dict_r = json.loads(str_r)
    #print(dict_r)
    #print(dict_r["result"]['songs'][0]['id'])
    ID=[dict_r["result"]['songs'][i]['id'] for i in range(0,len(dict_r["result"]['songs']))]
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
    time.sleep(0.2)
    url = "http://music.163.com/api/song/detail/?id={}&ids=%5B{}%5D".format(id,id)
    r = rs.get(url, headers=get_headers())
    r.encoding = 'utf-8'
    str_r = r.text
    dict_r = json.loads(str_r)
    print(dict_r)
    artists_name =  [x['name'] for x in dict_r['songs'][0]['artists']]
    
    #print(dict_r['songs'][0])
    #artists_name =  dict_r['songs'][0]['album']['name']
    return (dict_r['songs'][0]['name'],artists_name)

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
