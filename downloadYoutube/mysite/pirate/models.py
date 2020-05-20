from django.db import models

# Create your models here.
class Video(models.Model):
    link = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    Author = models.CharField(max_length=200)
    description = models.CharField(max_length=4000)
    name = models.CharField(max_length=400)

class Playlist(models.Model):
    Videos = models.ManyToManyField(Video)
    description = models.CharField(max_length=4000)

#python manage.py migrate --run-syncdb
