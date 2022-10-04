
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
    res = {}
    res['musicUrl'] = crawler.get_Music_url(name)
    print(get_Music_url('the show'))
    return JsonResponse(res)

#print(get_Music_url('the show'))