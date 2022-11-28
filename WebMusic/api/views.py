
from ast import match_case
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . import crawler
from django.views.decorators.http import require_http_methods
from django.core import serializers
from . import models
from django.contrib.auth import authenticate,login

import json
# Create your views here.
##
mp = {}
@require_http_methods(["GET","POST"])
def getMusic(request):
    print(request.body)
    if request.body in mp:
        return mp[request.body]
    dt = json.loads(request.body)
    name = dt['musicname']
    id_list = crawler.get_ID(name)
    res = {}
    res['music'] = [{
                    'id':id,
                    'name':crawler.get_Music_name(id),
                    'artists':crawler.get_artists_name(id),
                    'url':crawler.get_Music_url(id),
                    'pic_url':crawler.get_pic_url(id),
                    } for id in id_list]
    print(res)
    mp[request.body] = JsonResponse(res)
    return JsonResponse(res)

@require_http_methods(["GET","POST"])
def getLyric(request):
    # print(request.method)
    if(request.body in mp):
        return mp[request.body]
    try:
        dt = json.loads(request.body)
        id = dt['id']
    except:
        id = request.POST.get("id")
    # id=16607964
    # print(id)
    musicName=crawler.get_Music_name(id)
    musicLyric=crawler.get_lyric(id)
    # print(type(musicLyric))
    res = {}
    res['lyric'] = {
                    'id':id,
                    'musicLyric':musicLyric,
                    }
    # print(res)
    mp[request.body] = JsonResponse(res)
    return JsonResponse(res)


@require_http_methods(["GET","POST"])
def getHotlist(request):
    print(request.body)
    if request.body in mp:
        return mp[request.body]
    id_list = crawler.get_Hotlist()
    res = {}
    res['music'] = [{
                    'id':id,
                    'name':crawler.get_Music_name(id),
                    'artists':crawler.get_artists_name(id),
                    'url':crawler.get_Music_url(id),
                    'pic_url':crawler.get_pic_url(id),
                    } for id in id_list]
    print(res['music'])
    mp[request.body] = JsonResponse(res)
    return JsonResponse(res)
#print(get_Music_url('the show'))

@require_http_methods(["GET","POST"])
def mySignIn(request):
    print(request.body)
    
    dt = json.loads(request.body)
    user_name = dt['username']
    pass_word = dt['password']
    res = {}    
    if user_name and pass_word:
        user_name = user_name.strip()
        try:
            user = models.User.objects.get(name = user_name)
        except:
            res['auth'] = False
            res['message'] = 'error username'
            print('false')
            return JsonResponse(res)
        if user.password == pass_word:
            res['auth'] = True
            res['message'] = 'welcome to WebMusic'
            res['username'] = user_name
            return JsonResponse(res)
        else:
            res['auth'] = False
            res['message'] = 'error password'
            return JsonResponse(res)
    res['auth'] = False
    res['message'] = 'error username or password'
    return JsonResponse(res)
    
    #if user is not None:
    #    login(request,user)
@require_http_methods(["GET","POST"])
def mySignUp(request):
    print(request.body)
    dt = json.loads(request.body)
    user_name = dt['username']
    pass_word = dt['password']
    res = {}    
    if user_name and pass_word:
        user_name = user_name.strip()
        try:
            user = models.User.objects.get(name = user_name)
            res['auth'] = False
            res['message'] = 'repeated username'
            return JsonResponse(res)
        except:
            res['auth'] = True
            res['message'] = 'Welcome to WebMusic'
            user = models.User.objects.create()
            user.name = user_name
            user.password = pass_word
            user.save()
            res['username'] = user_name
            return JsonResponse(res)
    res['auth'] = False
    res['message'] = 'error username or password'
    return JsonResponse(res)
