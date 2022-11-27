
from django.db import models
 
 
class User(models.Model):
    '''用户表'''
 
    name = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=256)

 
    def __str__(self):
        return self.name
 
class screens(models.Model):
    '''弹幕'''

    music_id = models.CharField()
    screens_count = models.PositiveIntegerField()
    content = models.CharField(max_length=256)
    source = models.CharField(max_length=128,unique=True)
    '''source记录发送者用户名'''
    likes = models.PositiveIntegerField()
    dislikes = models.PositiveIntegerField()


