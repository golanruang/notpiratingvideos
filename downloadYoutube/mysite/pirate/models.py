from django.db import models

# Create your models here.
class Video(models.Model):
    link = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    Author = models.CharField(max_length=200)
    description = models.CharField(max_length=4000)
    name = models.CharField(max_length=400)

class Playlist(models.Model):
    Videos = models.ForeignKey(Video, on_delete=models.CASCADE)
    description = models.CharField(max_length=4000)
