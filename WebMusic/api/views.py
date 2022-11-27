from ast import match_case
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import crawler
from django.views.decorators.http import require_http_methods
from django.core import serializers
from . import models
from django.contrib.auth import authenticate, login

import json

# Create your views here.
##
mp = {}


@require_http_methods(["GET", "POST"])
def getMusic(request):
    print(request.body)
    if request.body in mp:
        return mp[request.body]
    dt = json.loads(request.body)
    name = dt['musicname']
    id_list = crawler.get_ID(name)
    res = {}
    res['music'] = [{
        'id': id,
        'name': crawler.get_Music_name(id),
        'artists': crawler.get_artists_name(id),
        'url': crawler.get_Music_url(id),
        'pic_url': crawler.get_pic_url(id),
    } for id in id_list]
    print(res)
    mp[request.body] = JsonResponse(res)
    return JsonResponse(res)


@require_http_methods(["GET", "POST"])
def getHotlist(request):
    print(request.body)
    if request.body in mp:
        return mp[request.body]
    id_list = crawler.get_Hotlist()
    res = {}
    res['music'] = [{
        'id': id,
        'name': crawler.get_Music_name(id),
        'artists': crawler.get_artists_name(id),
        'url': crawler.get_Music_url(id),
        'pic_url': crawler.get_pic_url(id),
    } for id in id_list]
    print(res['music'])
    mp[request.body] = JsonResponse(res)
    return JsonResponse(res)


# print(get_Music_url('the show'))

@require_http_methods(["GET", "POST"])
def mySignIn(request):
    print(request.body)

    dt = json.loads(request.body)
    user_name = dt['username']
    pass_word = dt['password']
    res = {}
    if user_name and pass_word:
        user_name = user_name.strip()
        try:
            user = models.User.objects.get(name=user_name)
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

    # if user is not None:
    #    login(request,user)


@require_http_methods(["GET", "POST"])
def mySignUp(request):
    print(request.body)
    dt = json.loads(request.body)
    user_name = dt['username']
    pass_word = dt['password']
    res = {}
    if user_name and pass_word:
        user_name = user_name.strip()
        try:
            user = models.User.objects.get(name=user_name)
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


sp = {}


@require_http_methods(["GET", "POST"])
def getscreens(request):
    print(request.body)
    dt = json.loads(request.body)
    music_id = dt['music_id']
    content = dt['content']
    source = dt['username']
    if music_id in sp:
        sp[music_id] = sp[music_id] + 1
    else:
        sp[music_id] = 0
    scr = {}
    scr['music_id'] = music_id
    scr['count'] = sp[music_id]
    scr['content'] = content
    scr['source'] = source
    scr['likes'] = 0
    scr['dislikes'] = 0
    obj = models.screens(**scr)
    obj.save()


@require_http_methods(["GET", "POST"])
def printscreens(request):
    print(request.body)
    dt = json.loads(request.body)
    t_music = dt['music_id']
    count = sp[t_music]
    screens = {}
    for i in range(1, count):
        obj = models.screens.objects.get(music_id = t_music, screens_count = i)
        screens[i] = obj
    return JsonResponse(screens)


@require_http_methods(["GET", "POST"])
def likescreens(request):
    print(request.body)
    dt = json.loads(request.body)
    t_music = dt['music_id']
    t_screen = dt['screens_count']
    obj = models.screens.objects.get(music_id = t_music, screens_count = t_screen)
    obj.likes = obj.likes + 1
    obj.save()


@require_http_methods(["GET", "POST"])
def dislikescreens(request):
    print(request.body)
    dt = json.loads(request.body)
    t_music = dt['music_id']
    t_screens = dt['screens_count']
    obj = models.screens.objects.get(music_id = t_music, screens_count = t_screen)
    obj.dislikes = obj.dislikes + 1
    obj.save()