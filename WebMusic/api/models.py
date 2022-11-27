
from django.db import models
import json
 
class User(models.Model):
    '''用户表'''
 
    name = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=256)
    likes = models.CharField(max_length = 200,default='[]')
    def get_likes(self):
        print(self.likes)
        return json.loads(self.likes)
    def add_likes(self,x):
        st = set(json.loads(self.likes))
        st = st | set([x])
        self.likes = json.dumps(list(st))
        print(self.likes)
        self.save()
        print(self.likes)
    def del_likes(self,x):
        st = set(json.loads(self.likes))
        st = st - set([x])
        self.likes = json.dumps(list(st))
        print(self.likes)
        self.save()
    def __str__(self):
        return self.name
    pass
 
       