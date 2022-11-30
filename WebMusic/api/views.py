
from ast import match_case
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .import crawler
from .import get_comment
from django.views.decorators.http import require_http_methods
from django.core import serializers
from . import models
from django.contrib.auth import authenticate,login
from multiprocessing import Pool#多进程池
from collections import ChainMap
import json
# Create your views here.
##
def getMusicbyId(id):
    namels = crawler.get_Music_name(id)
    return {
        'id':id,
        'name':namels[0],
        'artists':namels[1],
        'url':crawler.get_Music_url(id),
        'pic_url':crawler.get_pic_url(id),
    }
mp = {}
@require_http_methods(["GET","POST"])
def getMusic(request):
    print(request.body)
    print(request.POST)
    if request.body in mp:
        return mp[request.body]
    try:
        dt = json.loads(request.body)
    except:
        dt = request.POST
    name = dt['musicname']
    id_list = crawler.get_ID(name)
    res = {}
    res['music'] = [ getMusicbyId(id) for id in id_list]
    print(res)
    mp[request.body] = JsonResponse(res)
    return JsonResponse(res)

@require_http_methods(["GET","POST"])
def getHotlist(request):
    print(request.body)
    if request.body in mp:
        return mp[request.body]
    id_list = crawler.get_Hotlist()
    res = {}
    res['music'] = [ getMusicbyId(id) for id in id_list]
    print(res['music'])
    mp[request.body] = JsonResponse(res)
    return JsonResponse(res)
#print(get_Music_url('the show'))

@require_http_methods(["GET","POST"])
def mySignIn(request):
    print(request.body)
    
    try:
        dt = json.loads(request.body)
    except:
        dt = request.POST
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
    try:
        dt = json.loads(request.body)
    except:
        dt = request.POST
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
@require_http_methods(["GET","POST"])
def myLikes(request):
    print(request.body)
    try:
        dt = json.loads(request.body)
    except:
        dt = request.POST
    res = {}
    user_name = dt['username']
    res['exist'] = False
    try:
        user = models.User.objects.get(name = user_name)
    except:
        res['message'] = 'wrong user name'
        return JsonResponse(res)
    if dt['opt'] == 'add':
        user.add_likes(dt['id'])
        res['exist'] = True
    elif dt['opt'] == 'del':
        user.del_likes(dt['id'])
        res['exist'] = False
    elif dt['opt'] == 'queryid':
        res['exist'] = (dt['id'] in user.get_likes())
    elif dt['opt'] == 'queryall':
        res['music'] = [ getMusicbyId(int(id)) for id in user.get_likes()]
    user.save()
    res['message'] = 'done'
    print(user.get_likes())
    mp[request.body] = JsonResponse(res)
    return JsonResponse(res)

@require_http_methods(["GET","POST"])
def getComment(request):
    try:
        dt = json.loads(request.body)
    except:
        dt = request.POST
    id = dt['id']
    musicid = id
    data = []
    for x in range(0, 30):
        gethtml =get_comment.get_response(x, 30, str(musicid))
        data1 = get_comment.parse_return(gethtml)
        data.append(data1)
    return JsonResponse(data,safe=False)