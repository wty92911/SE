from django.db import models

# Create your models here.
class Mymusic(models.Model):
    url = models.CharField(max_length=1024)

    def __str__(self):
        return self.url