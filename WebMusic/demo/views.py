from ast import match_case
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .search import geturl
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
from .models import Mymusic
# Create your views here.
##
@require_http_methods(["GET","POST"])
def search(request):
    print(request.body)
    dt = json.loads(request.body)
    name = dt['musicname']
    res = {}
    music = []
    for x in geturl(name):
        music.append(Mymusic(url = x))
    res['list'] = json.loads(serializers.serialize('json',music))
    return JsonResponse(res)