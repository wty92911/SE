from django.urls import path
from .import views

urlpatterns = [
    path('getMusic1',views.getMusic,name = 'getMusic'),
    path('getHotlist1',views.getHotlist,name = 'getHotlist'),
    path('mySignIn',views.mySignIn,name='mySignIn'),
    path('mySignUp',views.mySignUp,name = 'mySignUp')
]