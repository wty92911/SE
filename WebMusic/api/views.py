
from ast import match_case
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .import crawler
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
# Create your views here.
##
@require_http_methods(["GET","POST"])
def getMusic(request):
    print(request.body)
    dt = json.loads(request.body)
    name = dt['musicname']
    id_list = crawler.get_ID(name)
    res = {}
    res['music'] = [{
                    'id':id,
                    'name':crawler.get_Music_name(id),
                    'artists':crawler.get_artists_name(id),
                    'url':crawler.get_Music_url(id)
                    } for id in id_list]
    return JsonResponse(res)

@require_http_methods(["GET","POST"])
def getHotlist(request):
    print(request.body)
    id_list = crawler.get_Hotlist()
    res = {}
    res['music'] = [{
                    'id':id,
                    'name':crawler.get_Music_name(id),
                    'artists':crawler.get_artists_name(id),
                    'url':crawler.get_Music_url(id),
                    'pic_url':crawler.get_pic_url(id)
                    } for id in id_list]
    print(res['music'])
    return JsonResponse(res)
#print(get_Music_url('the show'))