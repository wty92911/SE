from django.urls import path
from .import views

urlpatterns = [
    path('getMusic',views.getMusic,name = 'getMusic'),
]