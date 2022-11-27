from django.urls import path
from .import views

urlpatterns = [
    path('getMusic',views.getMusic,name = 'getMusic'),
    path('getHotlist',views.getHotlist,name = 'getHotlist'),
    path('mySignIn',views.mySignIn,name='mySignIn'),
    path('mySignUp',views.mySignUp,name = 'mySignUp'),
    path('getscreens',views.getscreens,name = 'getscreens'),
    path('likescreens',views.likescreens,name = 'likescreens'),
    path('dislikescreens',views.dislikescreens,name = 'dislikescreens'),
    path('printscreens',views.printscreens,name = 'printscreens'),
]